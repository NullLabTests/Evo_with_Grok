#!/usr/bin/env python3.11

import os
import sqlite3
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import random
from collections import deque
import requests
import psutil
from openai import OpenAI
import logging
import time
import ast
from datetime import datetime
import importlib.util

# --- Setup ---

# Load XAI_API_KEY from environment
XAI_API_KEY = os.getenv("XAI_API_KEY")
if not XAI_API_KEY:
    raise ValueError("XAI_API_KEY must be set in the environment")

# Initialize OpenAI client for xAI API
client = OpenAI(api_key=XAI_API_KEY, base_url="https://api.x.ai/v1")

# Set up logging
logging.basicConfig(filename="autoevolver.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Initialize database
conn = sqlite3.connect("autoevolver.db")
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS knowledge (
    key TEXT PRIMARY KEY,
    value TEXT,
    fetch_count INTEGER,
    last_fetched TIMESTAMP
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS tentacles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT,
    performance REAL,
    creation_time TIMESTAMP,
    parent_id INTEGER,
    domains TEXT
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS logs (
    timestamp TIMESTAMP,
    action TEXT,
    reward REAL,
    state TEXT
)
''')
conn.commit()

# Initialize tentacles dictionary
tentacles = {}

# Challenges list
challenges = [
    {"description": "convert the text to lowercase", "input": "Hello WORLD!", "expected": "helloworld!", "domain": "text processing"},
    {"description": "evaluate the mathematical expression", "input": "2 + 2", "expected": "4", "domain": "mathematics"},
    {"description": "determine if the statement is true or false", "input": "If A implies B and B implies C, then A implies C.", "expected": "True", "domain": "logic"},
    {"description": "sort the list of numbers", "input": "3,1,4,2", "expected": "1,2,3,4", "domain": "data analysis"},
    {"description": "extract URLs from the text", "input": "Visit https://x.ai for more info.", "expected": "https://x.ai", "domain": "text processing"},
    {"description": "count the number of words", "input": "This is a test.", "expected": "4", "domain": "text processing"},
    {"description": "check if the number is prime", "input": "7", "expected": "True", "domain": "mathematics"},
    {"description": "find the maximum in the list", "input": "[3,1,4,2]", "expected": "4", "domain": "data analysis"},
    {"description": "evaluate the logical expression", "input": "True and False", "expected": "False", "domain": "logic"},
    {"description": "solve the equation for x", "input": "2*x + 3 = 7", "expected": "2", "domain": "mathematics"},
    {"description": "parse and extract entities from text", "input": "John went to Paris.", "expected": "Person: John, Location: Paris", "domain": "natural language processing"},
]

# --- Deep Q-Network (DQN) ---

class DQN(nn.Module):
    def __init__(self, state_size, action_size):
        super(DQN, self).__init__()
        self.fc1 = nn.Linear(state_size, 64)
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, action_size)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        return self.fc3(x)

class DQNAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.memory = deque(maxlen=10000)
        self.gamma = 0.99  # Discount factor
        self.epsilon = 1.0  # Exploration rate
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.model = DQN(state_size, action_size)
        self.target_model = DQN(state_size, action_size)
        self.optimizer = optim.Adam(self.model.parameters(), lr=0.001)
        self.update_target_model()

    def update_target_model(self):
        self.target_model.load_state_dict(self.model.state_dict())

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state):
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size)
        state = torch.FloatTensor(state).unsqueeze(0)
        with torch.no_grad():
            q_values = self.model(state)
        return torch.argmax(q_values).item()

    def replay(self, batch_size):
        if len(self.memory) < batch_size:
            return
        minibatch = random.sample(self.memory, batch_size)
        for state, action, reward, next_state, done in minibatch:
            state = torch.FloatTensor(state).unsqueeze(0)
            next_state = torch.FloatTensor(next_state).unsqueeze(0)
            target = reward
            if not done:
                target = reward + self.gamma * torch.max(self.target_model(next_state)).item()
            target_f = self.model(state).detach().clone()
            target_f[0][action] = target
            loss = nn.MSELoss()(self.model(state), target_f)
            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

# --- Action Functions ---

def fetch_info():
    """Fetch and summarize a Wikipedia page using grok-2-latest."""
    try:
        # Find the minimum fetch_count
        min_fetch_count = cursor.execute('SELECT MIN(fetch_count) FROM knowledge').fetchone()[0]
        if min_fetch_count is None:
            logging.error("No topics found in knowledge table")
            return -1.0
        # Get all topics with that fetch_count
        cursor.execute('SELECT key FROM knowledge WHERE fetch_count = ?', (min_fetch_count,))
        topics = [row[0] for row in cursor.fetchall()]
        if not topics:
            logging.error("No topics found with minimum fetch_count")
            return -1.0
        # Randomly pick one topic
        topic = random.choice(topics)
        url = f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        content = response.text
        summary = client.chat.completions.create(
            model="grok-2-latest",
            messages=[{"role": "user", "content": f"Summarize this: {content[:1000]}"}]
        ).choices[0].message.content
        cursor.execute('UPDATE knowledge SET value = ?, fetch_count = fetch_count + 1, last_fetched = ? WHERE key = ?',
                       (summary, datetime.now(), topic))
        conn.commit()
        logging.info(f"Fetched topic: {topic}")
        return 1.0
    except Exception as e:
        logging.error(f"Fetch info failed: {e}")
        return -1.0

def evolve_tentacle():
    """Evolve tentacles using grok-2-latest with retry logic, duplication check, and challenge-based rewards."""
    max_retries = 3
    for attempt in range(max_retries):
        try:
            cursor.execute('SELECT id, code, domains FROM tentacles ORDER BY performance DESC LIMIT 2')
            parents = cursor.fetchall()
            if len(parents) < 2:
                logging.warning("Not enough tentacles to evolve")
                return -1.0
            parent1_id, parent1_code, parent1_domains = parents[0]
            parent2_id, parent2_code, parent2_domains = parents[1]
            parent1_domains = parent1_domains or "general"
            parent2_domains = parent2_domains or "general"
            all_domains = list(set(parent1_domains.split(',') + parent2_domains.split(',')))

            # Fetch knowledge based on domains
            placeholders = ','.join('?' * len(all_domains))
            cursor.execute(f'SELECT key, value FROM knowledge WHERE key IN ({placeholders})', all_domains)
            knowledge_entries = cursor.fetchall()
            knowledge_text = "\n".join([f"- From '{key}': {value[:200]}..." for key, value in knowledge_entries]) if knowledge_entries else "No relevant knowledge yet."

            # Select a random challenge
            challenge = random.choice(challenges)
            challenge_description = challenge['description']
            challenge_input = challenge['input']
            challenge_expected = challenge['expected']

            # Build prompt
            prompt = f"""Generate a new, valid Python function that combines or improves these tentacles. Ensure the code is executable, defines a function named 'tentacle', and aims to solve the following task: {challenge_description}. For example, given '{challenge_input}', it should return '{challenge_expected}'. Include a comment at the top like '# Domains: text processing, mathematics' based on functionality.

Parent Tentacles:
Tentacle 1 (domains: {parent1_domains}):
{parent1_code}

Tentacle 2 (domains: {parent2_domains}):
{parent2_code}

Relevant Knowledge:
{knowledge_text}"""

            # Generate new code
            response = client.chat.completions.create(
                model="grok-2-latest",
                messages=[{"role": "user", "content": prompt}]
            )
            new_code = response.choices[0].message.content.strip()
            if "```python" in new_code:
                new_code = new_code.split("```python")[1].split("```")[0].strip()

            # Validate syntax
            try:
                ast.parse(new_code)
            except SyntaxError as e:
                logging.error(f"Invalid syntax in generated code (attempt {attempt + 1}): {e}")
                continue

            # Check for duplication
            cursor.execute('SELECT id FROM tentacles WHERE code = ?', (new_code,))
            if cursor.fetchone():
                logging.info("Duplicate tentacle detected, skipping insertion")
                continue

            # Classify domains
            domain_prompt = f"Given this Python function, what domains does it relate to? Choose from: text processing, mathematics, logic, data analysis, machine learning, symbolic AI, game theory, natural language processing. Respond with a comma-separated list.\n\n{new_code}"
            domain_response = client.chat.completions.create(
                model="grok-2-latest",
                messages=[{"role": "user", "content": domain_prompt}]
            )
            domains = domain_response.choices[0].message.content.strip()

            # Test the tentacle
            local_vars = {}
            exec(new_code, {}, local_vars)
            tentacle_func = local_vars['tentacle']
            try:
                output = tentacle_func(challenge_input)
                if str(output) == challenge_expected:
                    reward = 5.0
                else:
                    reward = 1.0
            except Exception as e:
                logging.error(f"Tentacle execution failed: {e}")
                reward = -1.0
                continue

            # Insert into database
            performance = reward  # Use the reward as performance
            cursor.execute('INSERT INTO tentacles (code, performance, creation_time, parent_id, domains) VALUES (?, ?, ?, ?, ?)',
                           (new_code, performance, datetime.now(), parent1_id, domains))
            conn.commit()
            tentacle_id = cursor.lastrowid

            # Save and load the tentacle
            with open(f"tentacle_{tentacle_id}.py", "w") as f:
                f.write(new_code)
            spec = importlib.util.spec_from_file_location(f"tentacle_{tentacle_id}", f"tentacle_{tentacle_id}.py")
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            tentacles[f"tentacle_{tentacle_id}"] = module.tentacle
            logging.info(f"New tentacle evolved: tentacle_{tentacle_id} with domains: {domains}")
            return reward
        except Exception as e:
            logging.error(f"Evolve tentacle failed (attempt {attempt + 1}): {e}")
    logging.error("Max retries reached for evolve_tentacle")
    return -1.0

def optimize():
    """Manage system resources with proactive thresholds."""
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    reward = 0.1  # Small reward for monitoring
    if cpu > 60:
        agent.epsilon = min(1.0, agent.epsilon * 1.1)
        logging.info(f"Increased epsilon to {agent.epsilon} due to high CPU: {cpu}%")
        reward += 0.5
    if mem > 60:
        cursor.execute('DELETE FROM tentacles WHERE id = (SELECT id FROM tentacles ORDER BY performance ASC LIMIT 1)')
        conn.commit()
        deleted_id = cursor.execute('SELECT id FROM tentacles ORDER BY performance ASC LIMIT 1').fetchone()
        if deleted_id:
            tentacle_name = f"tentacle_{deleted_id[0]}"
            if tentacle_name in tentacles:
                del tentacles[tentacle_name]
            if os.path.exists(f"{tentacle_name}.py"):
                os.remove(f"{tentacle_name}.py")
        logging.info(f"Deleted lowest-performing tentacle due to high memory: {mem}%")
        reward += 0.5
    return reward

# --- State and Checkpointing ---

def get_state():
    """Retrieve the current system state."""
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    tentacle_count = cursor.execute('SELECT COUNT(*) FROM tentacles').fetchone()[0]
    knowledge_size = cursor.execute('SELECT COUNT(*) FROM knowledge').fetchone()[0]
    return np.array([cpu, mem, tentacle_count, knowledge_size], dtype=np.float32)

def save_checkpoint(agent):
    """Save the DQN model state."""
    torch.save(agent.model.state_dict(), "dqn_model.pt")
    logging.info("Checkpoint saved")

def load_checkpoint(agent):
    """Load the last saved DQN model state if available."""
    try:
        agent.model.load_state_dict(torch.load("dqn_model.pt"))
        agent.target_model.load_state_dict(torch.load("dqn_model.pt"))
        logging.info("Checkpoint loaded")
    except FileNotFoundError:
        logging.info("No checkpoint found, starting fresh")

def load_tentacles():
    """Load existing tentacles from the database."""
    cursor.execute('SELECT id, code FROM tentacles')
    for tentacle_id, code in cursor.fetchall():
        tentacle_file = f"tentacle_{tentacle_id}.py"
        if not os.path.exists(tentacle_file):
            with open(tentacle_file, "w") as f:
                f.write(code)
        spec = importlib.util.spec_from_file_location(f"tentacle_{tentacle_id}", tentacle_file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        tentacles[f"tentacle_{tentacle_id}"] = module.tentacle
    logging.info(f"Loaded {len(tentacles)} tentacles")

# --- Main Loop ---

agent = DQNAgent(state_size=4, action_size=3)  # Actions: [fetch_info, evolve_tentacle, optimize]
load_checkpoint(agent)
load_tentacles()

# Seed initial data if empty
if not cursor.execute('SELECT COUNT(*) FROM knowledge').fetchone()[0]:
    topics = ["Artificial Intelligence", "Symbolic Logic", "Mathematics", "Game Theory", "Natural Language Processing", "Machine Learning"]
    for topic in topics:
        cursor.execute('INSERT INTO knowledge (key, value, fetch_count, last_fetched) VALUES (?, ?, ?, ?)',
                       (topic, "", 0, datetime.now()))
    conn.commit()
    logging.info("Initialized knowledge with seed topics")

if cursor.execute('SELECT COUNT(*) FROM tentacles').fetchone()[0] < 2:
    cursor.execute('INSERT INTO tentacles (code, performance, creation_time, domains) VALUES (?, ?, ?, ?)',
                   ("def tentacle(input):\n    return input.lower()", 0.5, datetime.now(), "text processing"))
    cursor.execute('INSERT INTO tentacles (code, performance, creation_time, domains) VALUES (?, ?, ?, ?)',
                   ("def tentacle(input):\n    return input.upper()", 0.5, datetime.now(), "text processing"))
    conn.commit()
    logging.info("Initialized with default tentacles")

iteration = 0
try:
    while True:
        state = get_state()
        action = agent.act(state)
        if action == 0:
            reward = fetch_info()
            action_name = "fetch_info"
        elif action == 1:
            reward = evolve_tentacle()
            action_name = "evolve_tentacle"
        elif action == 2:
            reward = optimize()
            action_name = "optimize"
        next_state = get_state()
        agent.remember(state, action, reward, next_state, False)
        agent.replay(batch_size=32)
        if iteration % 100 == 0:
            agent.update_target_model()
            save_checkpoint(agent)
        logging.info(f"Iteration {iteration}: Action={action_name}, Reward={reward}, State={state.tolist()}")
        iteration += 1
        time.sleep(1)  # Prevent overloading
except KeyboardInterrupt:
    logging.info("Script stopped by user")
    save_checkpoint(agent)
finally:
    conn.close()

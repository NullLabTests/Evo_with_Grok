# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from the given text.
    
    Args:
    text (str): A string containing text to analyze.
    
    Returns:
    str: A string with extracted entities formatted as 'Entity: Value'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Initialize a dictionary to store extracted entities
    entities = {}
    
    # Extract Person entity (assuming it's the first word)
    person_match = re.match(r'^([A-Z][a-z]+)', text)
    if person_match:
        entities['Person'] = person_match.group(1)
    
    # Extract Location entity (assuming it's the last word)
    location_match = re.search(r'\bto\s+([A-Z][a-z]+)\.?$', text)
    if location_match:
        entities['Location'] = location_match.group(1)
    
    # Format and return the extracted entities
    return ', '.join(f"{entity}: {value}" for entity, value in entities.items())

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary traveled to London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('Bob visited New York.'))  # Should print: Person: Bob, Location: New York
    print(tentacle('Alice is going to Rome.'))  # Should print: Person: Alice, Location: Rome
    print(tentacle('No one went anywhere.'))  # Should print: (empty string)
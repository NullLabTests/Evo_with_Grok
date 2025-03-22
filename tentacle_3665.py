# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to parse for entities.
    
    Returns:
    str: A string with identified entities formatted as 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Define patterns and entity types
    patterns = {
        r'\b[A-Z][a-z]+\b': 'Person',
        r'\b(?:to|in|at)\s([A-Z][a-zA-Z]+)\b': 'Location'
    }
    
    entities = []
    
    for pattern, entity_type in patterns.items():
        matches = re.findall(pattern, text)
        for match in matches:
            entities.append(f"{entity_type}: {match}")
    
    # Join the identified entities
    return ', '.join(entities)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London and met with Alice.'))  # Should print: Person: Mary, Person: London, Person: Alice
    print(tentacle('In New York, Bob saw the Statue of Liberty.'))  # Should print: Location: New York, Person: Bob
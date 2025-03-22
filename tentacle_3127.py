# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to parse.
    
    Returns:
    str: A string with identified entities and their types.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Define patterns for entity extraction
    patterns = {
        'Person': r'\b[A-Z][a-z]+\b',
        'Location': r'\b(?:[A-Z][a-z]+)+\b'
    }
    
    # Initialize dictionary to store found entities
    entities = {}
    
    # Iterate through patterns and find matches
    for entity_type, pattern in patterns.items():
        matches = re.findall(pattern, text)
        if matches:
            entities[entity_type] = matches
    
    # Format the result string
    result = []
    for entity_type, names in entities.items():
        for name in names:
            result.append(f"{entity_type}: {name}")
    
    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited New York and London.'))  # Should print: Person: Mary, Location: New York, Location: London
    print(tentacle('No entities here.'))  # Should print: 
    print(tentacle('Alice and Bob went to Tokyo.'))  # Should print: Person: Alice, Person: Bob, Location: Tokyo
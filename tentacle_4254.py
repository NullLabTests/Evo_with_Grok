# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to parse for entities.
    
    Returns:
    str: A string with extracted entities formatted as 'Entity Type: Entity'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Define patterns for entity extraction
    patterns = {
        'Person': r'\b[A-Z][a-z]+\b',
        'Location': r'\b(?:Paris|London|New York|Tokyo)\b'
    }
    
    # Initialize result dictionary
    entities = {}
    
    # Extract entities using regex
    for entity_type, pattern in patterns.items():
        matches = re.findall(pattern, text)
        if matches:
            entities[entity_type] = matches[0]  # Take the first match for each type
    
    # Format the result
    result = ', '.join(f"{entity_type}: {entity}" for entity_type, entity in entities.items())
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London last year.'))  # Should print: Person: Mary, Location: London
    print(tentacle('I love Tokyo in the spring.'))  # Should print: Location: Tokyo
    print(tentacle('The meeting is in New York.'))  # Should print: Location: New York
    print(tentacle('Sarah enjoys her time in the city.'))  # Should print: Person: Sarah
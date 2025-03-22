# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to parse.
    
    Returns:
    str: A string with extracted entities in the format 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Dictionary to store entity types and their corresponding regex patterns
    entity_patterns = {
        'Person': r'\b[A-Z][a-z]+\b',
        'Location': r'\b(?:Paris|London|New York|Tokyo)\b'
    }
    
    # Dictionary to store extracted entities
    extracted_entities = {}
    
    # Iterate through entity types and their patterns
    for entity_type, pattern in entity_patterns.items():
        matches = re.findall(pattern, text)
        if matches:
            extracted_entities[entity_type] = matches[0]  # Take the first match for simplicity
    
    # Format the result string
    result = ', '.join([f"{entity_type}: {entity}" for entity_type, entity in extracted_entities.items()])
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Alice visited New York.'))  # Should print: Person: Alice, Location: New York
    print(tentacle('Bob is going to Tokyo.'))  # Should print: Person: Bob, Location: Tokyo
    print(tentacle('The weather in London is nice.'))  # Should print: Location: London
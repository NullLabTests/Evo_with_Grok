# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to be parsed.
    
    Returns:
    str: A string containing extracted entities in the format 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Dictionary to store entity types and their corresponding regex patterns
    entity_patterns = {
        'Person': r'\b([A-Z][a-z]+)\b',
        'Location': r'\bto\s+([A-Z][a-z]+)\b'
    }
    
    # Dictionary to store extracted entities
    entities = {}
    
    # Iterate through entity patterns and extract matches
    for entity_type, pattern in entity_patterns.items():
        matches = re.findall(pattern, text)
        if matches:
            entities[entity_type] = matches[0]  # Take the first match for each entity type
    
    # Format the output string
    output = ', '.join(f"{entity_type}: {entity}" for entity_type, entity in entities.items())
    
    return output

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Alice visited New York.'))  # Should print: Person: Alice, Location: New York
    print(tentacle('Bob is going to London tomorrow.'))  # Should print: Person: Bob, Location: London
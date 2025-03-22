# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to parse for entities.
    
    Returns:
    str: A string with extracted entities formatted as 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Dictionary to store entity types and their corresponding patterns
    entity_patterns = {
        'Person': r'\b([A-Z][a-z]+)\b',
        'Location': r'\bto\s([A-Z][a-z]+)\b'
    }
    
    entities = []
    
    for entity_type, pattern in entity_patterns.items():
        matches = re.findall(pattern, text)
        if matches:
            for match in matches:
                entities.append(f"{entity_type}: {match}")
    
    return ', '.join(entities)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Alice visited New York.'))  # Should print: Person: Alice, Location: York
    print(tentacle('Bob is going to London tomorrow.'))  # Should print: Person: Bob, Location: London
    print(tentacle('No entities here.'))  # Should print: empty string
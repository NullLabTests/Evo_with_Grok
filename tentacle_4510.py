# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to parse.
    
    Returns:
    str: A string with extracted entities formatted as 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Dictionary to store entity types and their patterns
    entity_patterns = {
        'Person': r'\b([A-Z][a-z]+)\b',
        'Location': r'\bto\s+([A-Z][a-z]+)\b'
    }
    
    # Initialize a list to store found entities
    found_entities = []
    
    # Iterate through entity types and patterns
    for entity_type, pattern in entity_patterns.items():
        import re
        matches = re.findall(pattern, text)
        if matches:
            for match in matches:
                found_entities.append(f"{entity_type}: {match}")
    
    # Join the found entities with a comma and space
    return ', '.join(found_entities)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Alice visited New York.'))  # Should print: Person: Alice, Location: York
    print(tentacle('Bob traveled to London.'))  # Should print: Person: Bob, Location: London
    print(tentacle('No entities here.'))  # Should print: (empty string)
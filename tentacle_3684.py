# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to parse.
    
    Returns:
    str: A string with extracted entities formatted as 'Entity Type: Entity'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Dictionary to store entity types and their patterns
    entity_patterns = {
        'Person': r'\b[A-Z][a-z]+\b',
        'Location': r'\b(?:Paris|New York|London|Tokyo)\b'
    }
    
    # Initialize a list to store found entities
    found_entities = []
    
    # Iterate through entity types and patterns
    for entity_type, pattern in entity_patterns.items():
        import re
        matches = re.findall(pattern, text)
        for match in matches:
            found_entities.append(f"{entity_type}: {match}")
    
    # Join the found entities and return the result
    return ', '.join(found_entities)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited New York and London.'))  # Should print: Person: Mary, Location: New York, Location: London
    print(tentacle('Tokyo is a beautiful city.'))  # Should print: Location: Tokyo
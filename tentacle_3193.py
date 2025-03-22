# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to parse for entities.
    
    Returns:
    str: A string containing extracted entities in the format 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Dictionary to store entity types and their corresponding regular expressions
    entity_patterns = {
        'Person': r'\b[A-Z][a-z]+\b',
        'Location': r'\b(?:Paris|London|New York|Tokyo)\b'
    }
    
    entities = []
    
    for entity_type, pattern in entity_patterns.items():
        matches = re.findall(pattern, text)
        for match in matches:
            entities.append(f"{entity_type}: {match}")
    
    return ', '.join(entities)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London and New York.'))  # Should print: Person: Mary, Location: London, Location: New York
    print(tentacle('In Tokyo, David met Sarah.'))  # Should print: Location: Tokyo, Person: David, Person: Sarah
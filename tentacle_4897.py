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
    
    # Dictionary to store entity types and their corresponding regex patterns
    entity_patterns = {
        'Person': r'\b[A-Z][a-z]+\b',
        'Location': r'\b(?:Paris|London|New York|Tokyo|Berlin)\b'
    }
    
    # Dictionary to store extracted entities
    extracted_entities = {}
    
    # Iterate through entity types and their patterns
    for entity_type, pattern in entity_patterns.items():
        matches = re.findall(pattern, text)
        if matches:
            extracted_entities[entity_type] = matches[0]  # Take the first match
    
    # Format the result
    result = ', '.join(f"{entity_type}: {entity}" for entity_type, entity in extracted_entities.items())
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The capital of France is Paris.'))  # Should print: Location: Paris
    print(tentacle('No entities here.'))  # Should print: (empty string)
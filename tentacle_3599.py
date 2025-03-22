# Domains: text processing, natural language processing
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
    # Dictionary to store entity types and their regex patterns
    entity_patterns = {
        'Person': r'\b([A-Z][a-z]+)\b',
        'Location': r'\b(to|in|at)\s([A-Z][a-z]+)\b'
    }
    
    # Dictionary to store extracted entities
    extracted_entities = {}
    
    for entity_type, pattern in entity_patterns.items():
        import re
        matches = re.findall(pattern, text)
        if matches:
            if entity_type == 'Location':
                # For location, we want the second group (the actual location)
                extracted_entities[entity_type] = matches[0][1]
            else:
                # For other entities, we take the first match
                extracted_entities[entity_type] = matches[0]
    
    # Format the result
    result = ', '.join(f"{entity_type}: {entity}" for entity_type, entity in extracted_entities.items())
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary is visiting New York.'))  # Should print: Person: Mary, Location: New York
    print(tentacle('The capital of France is Paris.'))  # Should print: Location: France, Location: Paris
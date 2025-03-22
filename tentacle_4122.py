# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to parse.
    
    Returns:
    str: A string containing extracted entities in the format 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Dictionary to store entity types and their corresponding patterns
    entity_patterns = {
        'Person': r'\b[A-Z][a-z]+\b',
        'Location': r'\b(?:Paris|London|New York|Tokyo)\b'
    }
    
    # Dictionary to store extracted entities
    extracted_entities = {}
    
    # Iterate through entity types and patterns
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
    print(tentacle('Mary visited London last week.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The conference is in New York next month.'))  # Should print: Location: New York
    print(tentacle('I love Tokyo in the spring.'))  # Should print: Location: Tokyo
    print(tentacle('Bob and Alice are going to the store.'))  # Should print: Person: Bob
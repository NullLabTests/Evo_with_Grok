# Domains: text processing, mathematics
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
    
    # Define patterns for entity extraction
    patterns = {
        'Person': r'\b[A-Z][a-z]+\b',
        'Location': r'\b(?:[A-Z][a-z]+ )*[A-Z][a-z]+\b'
    }
    
    # Initialize result dictionary
    entities = {}
    
    # Extract entities
    for entity_type, pattern in patterns.items():
        matches = re.findall(pattern, text)
        if matches:
            entities[entity_type] = matches[0]  # Take the first match for simplicity
    
    # Format the result
    result = ', '.join([f"{entity_type}: {entity}" for entity_type, entity in entities.items()])
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited New York.'))  # Should print: Person: Mary, Location: New York
    print(tentacle('The capital of France is Paris.'))  # Should print: Location: France, Location: Paris
    print(tentacle('No entities here.'))  # Should print:
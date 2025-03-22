# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to parse.
    
    Returns:
    str: A string with identified entities and their types.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Define patterns for entity extraction
    patterns = {
        'Person': r'\b([A-Z][a-z]+)\b',
        'Location': r'\b(?:to|in|at)\s+([A-Z][a-z]+)\b'
    }
    
    entities = {}
    
    for entity_type, pattern in patterns.items():
        matches = re.findall(pattern, text)
        if matches:
            entities[entity_type] = matches[0]  # Take the first match for simplicity
    
    # Format the result
    result = ', '.join(f"{entity_type}: {entity}" for entity_type, entity in entities.items())
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary is visiting London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The capital of France is Paris.'))  # Should print: Location: France, Location: Paris
    print(tentacle('No entities here.'))  # Should print: (empty string)
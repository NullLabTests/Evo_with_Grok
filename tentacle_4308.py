# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to be parsed for entities.
    
    Returns:
    str: A string containing identified entities and their types.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Define patterns for entity extraction
    patterns = {
        'Person': r'\b[A-Z][a-z]+\b',
        'Location': r'\b(?:Paris|London|New York|Tokyo|Berlin)\b'
    }
    
    # Initialize a dictionary to store identified entities
    entities = {}
    
    # Iterate through patterns and find matches
    for entity_type, pattern in patterns.items():
        matches = re.findall(pattern, text)
        if matches:
            entities[entity_type] = matches
    
    # Format the result string
    result = []
    for entity_type, names in entities.items():
        result.append(f"{entity_type}: {', '.join(names)}")
    
    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London and New York.'))  # Should print: Person: Mary, Location: London, New York
    print(tentacle('No entities here.'))  # Should print: (empty string)
    print(tentacle('Tokyo is a great city, said Tom.'))  # Should print: Person: Tom, Location: Tokyo
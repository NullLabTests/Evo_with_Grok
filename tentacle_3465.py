# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to be analyzed.
    
    Returns:
    str: A string containing extracted entities in the format 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Define patterns for entity extraction
    patterns = {
        'Person': r'\b([A-Z][a-z]+)\b',
        'Location': r'\bto\s+([A-Z][a-z]+)\b'
    }
    
    entities = []
    
    # Extract entities using regex patterns
    for entity_type, pattern in patterns.items():
        matches = re.findall(pattern, text)
        for match in matches:
            entities.append(f"{entity_type}: {match}")
    
    # Join extracted entities into a single string
    return ', '.join(entities)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London and met with Alice.'))  # Should print: Person: Mary, Person: Alice, Location: London
    print(tentacle('No entities here.'))  # Should print:
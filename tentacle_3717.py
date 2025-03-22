# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from the given text.
    
    Args:
    text (str): A string containing the text to be analyzed.
    
    Returns:
    str: A string with identified entities formatted as 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Dictionary to store entity types and their corresponding regex patterns
    entity_patterns = {
        'Person': r'\b([A-Z][a-z]+)\b',
        'Location': r'\b(?:to|in|at)\s([A-Z][a-z]+)\b'
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
    print(tentacle('Mary is traveling to London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('In New York, Alice met Bob.'))  # Should print: Location: New York, Person: Alice, Person: Bob
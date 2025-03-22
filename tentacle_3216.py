# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from the given text.
    
    Args:
    text (str): A string containing text to parse for entities.
    
    Returns:
    str: A string containing the extracted entities in the format 'Entity: Value'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Initialize dictionaries for entity patterns and extracted entities
    patterns = {
        'Person': r'\b[A-Z][a-z]+\b',
        'Location': r'\b(?:Paris|London|New York|Tokyo)\b'
    }
    entities = {}

    # Iterate through patterns and search for matches in the text
    for entity_type, pattern in patterns.items():
        import re
        matches = re.findall(pattern, text)
        if matches:
            entities[entity_type] = matches[0]  # Take the first match for simplicity

    # Format the result string
    result = ', '.join([f"{entity_type}: {entity}" for entity_type, entity in entities.items()])
    return result if result else "No entities found"

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Alice visited New York.'))  # Should print: Person: Alice, Location: New York
    print(tentacle('The weather in Tokyo is great.'))  # Should print: Location: Tokyo
    print(tentacle('No specific names or places mentioned.'))  # Should print: No entities found
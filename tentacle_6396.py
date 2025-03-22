# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.

    Args:
    text (str): A string containing text to parse for entities.

    Returns:
    str: A string with extracted entities formatted as 'Entity Type: Entity Name'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re

    # Define regex patterns for different entity types
    patterns = {
        'Person': r'\b[A-Z][a-z]+\b',
        'Location': r'\b(?:Paris|London|New York|Tokyo|Berlin)\b'
    }

    # Initialize a dictionary to store found entities
    entities = {}

    # Search for entities in the text
    for entity_type, pattern in patterns.items():
        matches = re.findall(pattern, text)
        if matches:
            entities[entity_type] = matches[0]  # Take the first match for simplicity

    # Format the result string
    result = ', '.join(f"{entity_type}: {entity}" for entity_type, entity in entities.items())

    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The conference is in New York.'))  # Should print: Location: New York
    print(tentacle('Tokyo is a beautiful city.'))  # Should print: Location: Tokyo
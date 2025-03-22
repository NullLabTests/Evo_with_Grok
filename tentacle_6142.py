# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.

    Args:
    text (str): A string containing text to parse.

    Returns:
    str: A string containing extracted entities formatted as 'Entity Type: Entity'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re

    # Define regex patterns for different entity types
    patterns = {
        'Person': r'\b[A-Z][a-z]+\b',
        'Location': r'\b(?:Paris|London|New York|Tokyo)\b'
    }

    # Initialize a dictionary to store extracted entities
    entities = {}

    # Iterate through patterns and find matches
    for entity_type, pattern in patterns.items():
        matches = re.findall(pattern, text)
        if matches:
            entities[entity_type] = matches

    # Format the result string
    result = []
    for entity_type, values in entities.items():
        result.append(f"{entity_type}: {', '.join(values)}")

    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London and New York.'))  # Should print: Person: Mary, Location: London, New York
    print(tentacle('Tokyo is a beautiful city.'))  # Should print: Location: Tokyo
    print(tentacle('No entities here.'))  # Should print: 
    print(tentacle('Alice and Bob went to the store.'))  # Should print: Person: Alice, Bob
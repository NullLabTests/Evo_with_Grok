# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.

    Args:
    text (str): A string containing text to parse.

    Returns:
    str: A string with extracted entities formatted as 'Entity Type: Entity Name'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re

    # Define patterns for entity extraction
    patterns = {
        'Person': r'\b[A-Z][a-z]+\b',
        'Location': r'\b(?:to|in|at)\s([A-Z][a-z]+)\b'
    }

    # Initialize dictionary to store extracted entities
    entities = {}

    # Extract entities based on defined patterns
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
    print(tentacle('Mary is visiting New York.'))  # Should print: Person: Mary, Location: York
    print(tentacle('The weather in London is great today.'))  # Should print: Location: London
# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.

    Args:
    text (str): A string containing text to parse for entities.

    Returns:
    str: A string containing identified entities in the format 'Entity Type: Entity Name'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re

    # Define patterns for entity extraction
    patterns = {
        'Person': r'\b([A-Z][a-z]+)\b',
        'Location': r'\b(?:to|in|at)\s([A-Z][a-z]+)\b'
    }

    # Initialize a dictionary to store extracted entities
    entities = {}

    # Iterate through patterns and extract matches
    for entity_type, pattern in patterns.items():
        matches = re.findall(pattern, text)
        if matches:
            entities[entity_type] = matches[0]  # Use the first match for simplicity

    # Format the result
    result = ', '.join([f"{entity_type}: {entity}" for entity_type, entity in entities.items()])

    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary is traveling to London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The meeting is in New York.'))  # Should print: Location: New York
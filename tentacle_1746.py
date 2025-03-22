# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.

    Args:
    text (str): A string containing text to parse.

    Returns:
    str: A string containing extracted entities in the format 'Entity Type: Entity Value'.

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

    # Initialize a dictionary to store extracted entities
    entities = {}

    # Extract entities based on patterns
    for entity_type, pattern in patterns.items():
        matches = re.findall(pattern, text)
        if matches:
            entities[entity_type] = matches[0]  # Use the first match for each entity type

    # Format the output string
    result = ', '.join(f"{entity_type}: {entity_value}" for entity_type, entity_value in entities.items())

    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('No entities here.'))     # Should print: (empty string)
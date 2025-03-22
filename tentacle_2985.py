# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.

    Args:
    text (str): A string containing text to parse for entities.

    Returns:
    str: A string with identified entities and their types.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re

    # Define patterns for entity recognition
    patterns = {
        'Person': r'\b[A-Z][a-z]+\b',
        'Location': r'\b(?:Paris|London|New York|Tokyo)\b'
    }

    # Initialize a dictionary to store found entities
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

    return ', '.join(result) if result else "No entities found."

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London and Tokyo.'))  # Should print: Person: Mary, Location: London, Tokyo
    print(tentacle('No names or locations here.'))  # Should print: No entities found.
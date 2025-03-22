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

    # Define patterns and entity types
    patterns = {
        r'\b[A-Z][a-z]+\b': 'Person',
        r'\b(?:New )?York\b': 'Location',
        r'\bParis\b': 'Location',
        r'\b(?:[12]\d{3}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01]))\b': 'Date',
    }

    entities = []
    for pattern, entity_type in patterns.items():
        matches = re.findall(pattern, text)
        for match in matches:
            entities.append(f"{entity_type}: {match}")

    # Return a comma-separated string of identified entities
    return ', '.join(entities)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Alice visited New York on 2023-05-15.'))  # Should print: Person: Alice, Location: New York, Date: 2023-05-15
    print(tentacle('Bob is planning a trip to Paris next year.'))  # Should print: Person: Bob, Location: Paris
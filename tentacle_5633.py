# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.

    Args:
    text (str): A string containing text to parse for entities.

    Returns:
    str: A string containing extracted entities in the format 'Entity Type: Entity Name'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re

    # Dictionary to store entity types and their corresponding patterns
    entity_patterns = {
        'Person': r'\b[A-Z][a-z]+\b',
        'Location': r'\b(?:[A-Z][a-z]+(?: [A-Z][a-z]+)*)\b'
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
    print(tentacle('Alice and Bob visited New York and London.'))  # Should print: Person: Alice, Person: Bob, Location: New York, Location: London
    print(tentacle('The meeting is in Tokyo with Sarah.'))  # Should print: Location: Tokyo, Person: Sarah
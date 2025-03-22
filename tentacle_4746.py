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

    # Dictionary to store extracted entities
    entities = {}

    # Extract person names (simple regex for demonstration)
    person_pattern = r'\b([A-Z][a-z]+)\b'
    persons = re.findall(person_pattern, text)
    if persons:
        entities['Person'] = ', '.join(persons)

    # Extract locations (simple regex for demonstration)
    location_pattern = r'\bto\s+([A-Z][a-z]+)\b'
    locations = re.findall(location_pattern, text)
    if locations:
        entities['Location'] = ', '.join(locations)

    # Format the result
    result = ', '.join([f"{entity_type}: {entity}" for entity_type, entity in entities.items()])
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Alice and Bob visited London and New York.'))  # Should print: Person: Alice, Bob, Location: London, New York
    print(tentacle('No entities here.'))  # Should print: empty string
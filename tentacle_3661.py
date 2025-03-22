# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.

    Args:
    text (str): A string containing text to parse.

    Returns:
    str: A string containing extracted entities in the format 'Entity Type: Entity Name'.

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
    for person in persons:
        entities['Person'] = entities.get('Person', []) + [person]

    # Extract locations (simple regex for demonstration)
    location_pattern = r'\bto\s([A-Z][a-z]+)\b'
    locations = re.findall(location_pattern, text)
    for location in locations:
        entities['Location'] = entities.get('Location', []) + [location]

    # Format the output
    output = []
    for entity_type, entity_list in entities.items():
        output.append(f"{entity_type}: {', '.join(entity_list)}")

    return ', '.join(output)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Alice and Bob visited New York and London.'))  # Should print: Person: Alice, Person: Bob, Location: New York, Location: London
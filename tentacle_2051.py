# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.

    Args:
    text (str): A string containing text to be parsed.

    Returns:
    str: A string containing extracted entities in the format 'Entity Type: Entity Name'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re

    # Initialize a dictionary to store entities
    entities = {}

    # Extract person names (assuming simple case of first word being a name)
    person_match = re.match(r'^([A-Z][a-z]+)\b', text)
    if person_match:
        entities['Person'] = person_match.group(1)

    # Extract location names (assuming last word being a location)
    location_match = re.search(r'\b([A-Z][a-z]+)\.$', text)
    if location_match:
        entities['Location'] = location_match.group(1)

    # Format and return the result
    return ', '.join(f"{entity_type}: {entity_name}" for entity_type, entity_name in entities.items())

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Alice visited New York.'))  # Should print: Person: Alice, Location: York
    print(tentacle('The capital is Berlin.'))  # Should print: Location: Berlin
    print(tentacle('Sarah likes hiking.'))  # Should print: Person: Sarah
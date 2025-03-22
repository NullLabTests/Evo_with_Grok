# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.

    Args:
    text (str): A string containing text to parse.

    Returns:
    str: A string with identified entities formatted as 'Entity Type: Entity Name'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re

    # Dictionary to store identified entities
    entities = {}

    # Regular expressions for entity extraction
    person_pattern = r'\b([A-Z][a-z]+)\b'
    location_pattern = r'\bto\s+([A-Z][a-z]+)\b'

    # Extract person names
    person_matches = re.findall(person_pattern, text)
    if person_matches:
        entities['Person'] = person_matches[0]

    # Extract location names
    location_matches = re.findall(location_pattern, text)
    if location_matches:
        entities['Location'] = location_matches[0]

    # Format the output
    return ', '.join(f"{entity_type}: {entity}" for entity_type, entity in entities.items())

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Alice visited New York.'))  # Should print: Person: Alice, Location: New York
    print(tentacle('The capital of France is Paris.'))  # Should print: Location: France, Location: Paris
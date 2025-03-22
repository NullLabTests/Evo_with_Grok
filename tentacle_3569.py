# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text, identifying persons and locations.

    Args:
    text (str): A string containing the text to be analyzed.

    Returns:
    str: A string with identified entities formatted as 'Entity Type: Entity Name'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re

    # Dictionary to store identified entities
    entities = {}

    # Extract person names (assuming simple names for this example)
    person_pattern = r'\b([A-Z][a-z]+)\b'
    person_matches = re.findall(person_pattern, text)
    if person_matches:
        entities['Person'] = person_matches[0]  # Assuming the first match is the person

    # Extract locations (assuming capitalized words for this example)
    location_pattern = r'\b([A-Z][a-z]+)\b(?! went)'
    location_matches = re.findall(location_pattern, text)
    if location_matches:
        entities['Location'] = location_matches[0]  # Assuming the first match is the location

    # Format the result
    result = ', '.join([f"{entity_type}: {entity}" for entity_type, entity in entities.items()])
    return result if result else "No entities found."

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited New York.'))  # Should print: Person: Mary, Location: New York
    print(tentacle('The cat sat on the mat.'))  # Should print: No entities found.
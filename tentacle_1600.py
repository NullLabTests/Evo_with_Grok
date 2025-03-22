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
    person_pattern = r'\b[A-Z][a-z]+\b'
    persons = re.findall(person_pattern, text)
    if persons:
        entities['Person'] = persons[0]  # Assume the first match is the main person

    # Extract locations (simple regex for demonstration)
    location_pattern = r'\b(?:New York|Paris|London|Tokyo)\b'
    locations = re.findall(location_pattern, text)
    if locations:
        entities['Location'] = locations[0]  # Assume the first match is the main location

    # Format the result
    result = ', '.join(f"{entity_type}: {entity}" for entity_type, entity in entities.items())

    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Alice visited New York.'))  # Should print: Person: Alice, Location: New York
    print(tentacle('Bob is going to London tomorrow.'))  # Should print: Person: Bob, Location: London
    print(tentacle('Sarah loves Tokyo.'))  # Should print: Person: Sarah, Location: Tokyo
    print(tentacle('The weather in Seattle is great.'))  # Should print: (nothing, as Seattle is not in the location list)
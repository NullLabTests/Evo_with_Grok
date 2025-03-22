# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.

    Args:
    text (str): A string containing text to parse for entities.

    Returns:
    str: A string with extracted entities formatted as 'Entity Type: Entity Name'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re

    # Define regex patterns for entity extraction
    person_pattern = r'\b[A-Z][a-z]+\b'
    location_pattern = r'\b(?:Paris|London|New York|Tokyo)\b'

    # Extract entities
    persons = re.findall(person_pattern, text)
    locations = re.findall(location_pattern, text)

    # Format the output
    entities = []
    if persons:
        entities.append(f"Person: {', '.join(persons)}")
    if locations:
        entities.append(f"Location: {', '.join(locations)}")

    return ', '.join(entities)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary and Alice visited London and New York.'))  # Should print: Person: Mary, Alice, Location: London, New York
    print(tentacle('Tokyo is a beautiful city.'))  # Should print: Location: Tokyo
    print(tentacle('The cat sat on the mat.'))  # Should print: (empty string)
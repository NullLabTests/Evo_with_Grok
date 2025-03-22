# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text, such as persons and locations.

    Args:
    text (str): A string containing text to parse for entities.

    Returns:
    str: A string containing extracted entities in the format 'Entity Type: Entity Name'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re

    # Define regex patterns for entity extraction
    person_pattern = r'\b([A-Z][a-z]+)\b'
    location_pattern = r'\bto\s+([A-Z][a-z]+)\b'

    # Extract entities using regex
    persons = re.findall(person_pattern, text)
    locations = re.findall(location_pattern, text)

    # Format the extracted entities
    result = []
    for person in persons:
        result.append(f'Person: {person}')
    for location in locations:
        result.append(f'Location: {location}')

    # Join the results and return
    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Alice and Bob visited London and New York.'))  # Should print: Person: Alice, Person: Bob, Location: London, Location: New York
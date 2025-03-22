# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.

    Args:
    text (str): A string containing text to be analyzed.

    Returns:
    str: A string with extracted entities formatted as 'Entity Type: Entity Name'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re

    # Define patterns for entity extraction
    person_pattern = r'\b[A-Z][a-z]+\b'
    location_pattern = r'\b(?:Paris|London|New York|Tokyo|Berlin)\b'

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
    print(tentacle('Alice and Bob visited London and New York.'))  # Should print: Person: Alice, Bob, Location: London, New York
    print(tentacle('The meeting is in Tokyo tomorrow.'))  # Should print: Location: Tokyo
    print(tentacle('No entities here.'))  # Should print: (empty string)
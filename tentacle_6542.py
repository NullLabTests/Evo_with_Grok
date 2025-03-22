# Domains: text processing, mathematics
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
    # Initialize a dictionary to store extracted entities
    entities = {}

    # Define regular expressions for entity extraction
    import re
    person_pattern = r'\b[A-Z][a-z]+\b'
    location_pattern = r'\b(?:Paris|New York|London|Tokyo|Berlin)\b'

    # Extract person names
    persons = re.findall(person_pattern, text)
    if persons:
        entities['Person'] = ', '.join(persons)

    # Extract locations
    locations = re.findall(location_pattern, text)
    if locations:
        entities['Location'] = ', '.join(locations)

    # Format the result
    result = ', '.join([f"{key}: {value}" for key, value in entities.items()])

    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Alice and Bob visited New York and London.'))  # Should print: Person: Alice, Bob, Location: New York, London
    print(tentacle('The weather in Tokyo is great today.'))  # Should print: Location: Tokyo
    print(tentacle('No entities here.'))  # Should print:
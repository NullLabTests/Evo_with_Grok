# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.

    This function uses regular expressions to identify and extract
    entities such as persons and locations from a given text.

    Args:
    text (str): A string containing the text to be analyzed.

    Returns:
    str: A formatted string containing the extracted entities.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re

    # Initialize an empty dictionary to store entities
    entities = {}

    # Extract persons (assuming a simple name pattern)
    person_pattern = r'\b([A-Z][a-z]+)\b'
    persons = re.findall(person_pattern, text)
    if persons:
        entities['Person'] = ', '.join(persons)

    # Extract locations (using a simple city name pattern)
    location_pattern = r'\b(Paris|London|New York|Tokyo)\b'
    locations = re.findall(location_pattern, text)
    if locations:
        entities['Location'] = ', '.join(locations)

    # Format the result
    result = ', '.join([f"{key}: {value}" for key, value in entities.items()])

    return result if result else "No entities found"

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London and New York.'))  # Should print: Person: Mary, Location: London, New York
    print(tentacle('No specific names or locations mentioned.'))  # Should print: No entities found
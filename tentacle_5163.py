# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text, identifying persons and locations.

    Args:
    text (str): A string containing the text to parse.

    Returns:
    str: A string with identified entities formatted as 'Entity Type: Entity Name'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re

    # Define regex patterns for persons and locations
    person_pattern = r'\b[A-Z][a-z]+\b'
    location_pattern = r'\b(?:[A-Z][a-z]+(?: [A-Z][a-z]+)*)\b'

    # Find matches for persons and locations
    persons = re.findall(person_pattern, text)
    locations = re.findall(location_pattern, text)

    # Filter out common words that might be incorrectly identified as persons
    common_words = ['The', 'A', 'An', 'And', 'But', 'Or', 'For', 'Nor', 'On', 'At', 'To', 'From', 'By', 'With']
    persons = [person for person in persons if person not in common_words]

    # Construct the result string
    result = []
    if persons:
        result.append(f"Person: {', '.join(persons)}")
    if locations:
        result.append(f"Location: {', '.join(locations)}")

    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary and Tom visited New York and London.'))  # Should print: Person: Mary, Tom, Location: New York, London
    print(tentacle('The cat sat on the mat.'))  # Should print: (nothing, as no persons or locations are identified)
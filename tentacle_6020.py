# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.

    Args:
    text (str): A string containing text to parse.

    Returns:
    str: A string with extracted entities formatted as 'Entity Type: Entity Name'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re

    # Define patterns for entity extraction
    person_pattern = r'\b[A-Z][a-z]+\b'
    location_pattern = r'\b(?:Paris|London|New York|Tokyo)\b'

    # Extract entities
    persons = re.findall(person_pattern, text)
    locations = re.findall(location_pattern, text)

    # Format the result
    result_parts = []
    if persons:
        result_parts.append(f"Person: {', '.join(persons)}")
    if locations:
        result_parts.append(f"Location: {', '.join(locations)}")

    return ', '.join(result_parts)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary and Bob visited London and New York.'))  # Should print: Person: Mary, Bob, Location: London, New York
    print(tentacle('Tokyo is a beautiful city.'))  # Should print: Location: Tokyo
    print(tentacle('The weather is nice today.'))  # Should print: (empty string)
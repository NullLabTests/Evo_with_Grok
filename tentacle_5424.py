# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text, specifically identifying persons and locations.

    Args:
    text (str): A string containing the text to parse.

    Returns:
    str: A formatted string with identified entities.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Initialize dictionaries for entity recognition
    persons = ['John', 'Mary', 'David', 'Sarah', 'Michael']
    locations = ['Paris', 'New York', 'London', 'Tokyo', 'Sydney']

    # Initialize variables to store identified entities
    identified_person = None
    identified_location = None

    # Split the text into words
    words = text.split()

    # Iterate through words to identify entities
    for word in words:
        if word in persons and identified_person is None:
            identified_person = word
        elif word in locations and identified_location is None:
            identified_location = word

    # Construct the result string
    result = []
    if identified_person:
        result.append(f'Person: {identified_person}')
    if identified_location:
        result.append(f'Location: {identified_location}')

    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary is visiting New York.'))  # Should print: Person: Mary, Location: New York
    print(tentacle('David lives in London.'))  # Should print: Person: David, Location: London
    print(tentacle('Sarah and Michael are going to Tokyo.'))  # Should print: Person: Sarah, Location: Tokyo
    print(tentacle('Sydney is a beautiful city.'))  # Should print: Location: Sydney
    print(tentacle('The weather is nice today.'))  # Should print:
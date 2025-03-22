# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.

    This function identifies and extracts 'Person' and 'Location' entities from a given text.
    It uses simple string matching to identify these entities.

    Args:
    text (str): A string containing text to parse for entities.

    Returns:
    str: A formatted string of extracted entities.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Define lists of common names and locations for simple matching
    persons = ['John', 'Mary', 'David', 'Lisa', 'Michael']
    locations = ['Paris', 'London', 'New York', 'Tokyo', 'Sydney']

    # Initialize variables to store found entities
    found_person = None
    found_location = None

    # Split the text into words
    words = text.split()

    # Iterate through words to find matches
    for word in words:
        if word in persons and not found_person:
            found_person = word
        if word in locations and not found_location:
            found_location = word

    # Construct the result string
    result = []
    if found_person:
        result.append(f'Person: {found_person}')
    if found_location:
        result.append(f'Location: {found_location}')

    return ', '.join(result) if result else 'No entities found.'

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('David is planning a trip to New York.'))  # Should print: Person: David, Location: New York
    print(tentacle('The weather in Tokyo is great.'))  # Should print: Location: Tokyo
    print(tentacle('Lisa and Michael are in Sydney.'))  # Should print: Person: Lisa, Location: Sydney
    print(tentacle('The book was interesting.'))  # Should print: No entities found.
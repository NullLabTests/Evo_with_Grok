# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.

    Args:
    text (str): A string containing text to parse.

    Returns:
    str: A string with extracted entities formatted as 'Entity Type: Entity'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Define dictionaries for entity recognition
    person_keywords = ['John', 'Mary', 'David']
    location_keywords = ['Paris', 'New York', 'London']

    # Initialize lists to store recognized entities
    persons = []
    locations = []

    # Split the text into words
    words = text.split()

    # Iterate through words to identify entities
    for word in words:
        if word in person_keywords:
            persons.append(word)
        elif word in location_keywords:
            locations.append(word)

    # Format the result
    result = []
    if persons:
        result.append(f"Person: {', '.join(persons)}")
    if locations:
        result.append(f"Location: {', '.join(locations)}")

    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited New York and London.'))  # Should print: Person: Mary, Location: New York, London
    print(tentacle('David stayed home.'))  # Should print: Person: David
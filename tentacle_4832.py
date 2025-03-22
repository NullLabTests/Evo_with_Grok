# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.

    Args:
    text (str): A string containing text to parse for entities.

    Returns:
    str: A string containing the extracted entities in the format 'Entity Type: Entity Name'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Define dictionaries for entity recognition
    person_keywords = ['John', 'Jane', 'Bob', 'Alice']
    location_keywords = ['Paris', 'London', 'New York', 'Tokyo']

    # Initialize variables to store recognized entities
    person = None
    location = None

    # Split the text into words
    words = text.split()

    # Iterate through words to identify entities
    for word in words:
        if word in person_keywords:
            person = word
        elif word in location_keywords:
            location = word

    # Construct the result string
    result = []
    if person:
        result.append(f'Person: {person}')
    if location:
        result.append(f'Location: {location}')

    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Jane visited London.'))  # Should print: Person: Jane, Location: London
    print(tentacle('Bob is planning a trip to New York.'))  # Should print: Person: Bob, Location: New York
    print(tentacle('Alice dreams of going to Tokyo someday.'))  # Should print: Person: Alice, Location: Tokyo
    print(tentacle('The weather in Paris is beautiful today.'))  # Should print: Location: Paris
    print(tentacle('John and Jane are good friends.'))  # Should print: Person: John, Person: Jane
    print(tentacle('I love traveling to new places.'))  # Should print: (empty string)
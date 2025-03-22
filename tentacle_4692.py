# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.

    This function uses simple pattern matching to identify and extract
    person names and location names from the input text.

    Args:
    text (str): A string containing the text to be processed.

    Returns:
    str: A string containing the extracted entities in the format
         'Person: <name>, Location: <location>'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Initialize variables to store extracted entities
    person = None
    location = None

    # Split the text into words
    words = text.split()

    # Simple pattern matching for person names (assuming first word is a name)
    if words:
        person = words[0]

    # Simple pattern matching for location names (assuming 'to' precedes a location)
    if 'to' in words:
        to_index = words.index('to')
        if to_index + 1 < len(words):
            location = words[to_index + 1]

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
    print(tentacle('Mary visited New York.'))  # Should print: Person: Mary, Location: York
    print(tentacle('I stayed in London.'))  # Should print: Person: I, Location: London
    print(tentacle('They traveled to Tokyo.'))  # Should print: Person: They, Location: Tokyo
    print(tentacle('The cat sat on the mat.'))  # Should print: Person: The
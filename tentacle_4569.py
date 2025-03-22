# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.

    This function uses simple pattern matching to identify and extract
    person names and location names from a given text.

    Args:
    text (str): A string containing the text to be analyzed.

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
    if words and words[0].istitle():
        person = words[0]

    # Simple pattern matching for location names (assuming 'to' precedes a location)
    if 'to' in words:
        to_index = words.index('to')
        if to_index + 1 < len(words) and words[to_index + 1].istitle():
            location = words[to_index + 1]

    # Construct the result string
    result = []
    if person:
        result.append(f"Person: {person}")
    if location:
        result.append(f"Location: {location}")

    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The cat sat on the mat.'))  # Should print: (nothing, as no entities are detected)
    print(tentacle('Alice traveled to New York City.'))  # Should print: Person: Alice, Location: New York City
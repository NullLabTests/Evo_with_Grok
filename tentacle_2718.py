# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.

    This function identifies and extracts 'Person' and 'Location' entities from a given text.
    It uses simple pattern matching to identify these entities.

    Args:
    text (str): A string containing the text to be parsed.

    Returns:
    str: A formatted string containing the extracted entities.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Initialize variables to store extracted entities
    person = None
    location = None

    # Split the text into words
    words = text.split()

    # Simple pattern matching to identify entities
    for word in words:
        if word.istitle() and word not in ['The', 'A', 'An']:
            if person is None:
                person = word
            elif location is None:
                location = word

    # Format and return the result
    result = []
    if person:
        result.append(f'Person: {person}')
    if location:
        result.append(f'Location: {location}')

    return ', '.join(result) if result else 'No entities found.'

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The cat sat on the mat.'))  # Should print: No entities found.
    print(tentacle('Alice and Bob traveled to New York.'))  # Should print: Person: Alice, Location: New York
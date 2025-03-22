# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from a given text.

    Args:
    text (str): A string containing text to parse for entities.

    Returns:
    str: A string containing the extracted entities formatted as 'Entity: Value'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Initialize variables to store extracted entities
    person = None
    location = None

    # Split the text into words
    words = text.split()

    # Simple rules to identify entities
    for word in words:
        if word.istitle() and word not in ['To', 'The', 'A', 'An']:
            if person is None:
                person = word
            elif location is None:
                location = word

    # Construct the result string
    result = []
    if person:
        result.append(f'Person: {person}')
    if location:
        result.append(f'Location: {location}')

    return ', '.join(result) if result else 'No entities found.'

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited New York.'))  # Should print: Person: Mary, Location: York
    print(tentacle('The cat sat on the mat.'))  # Should print: No entities found.
    print(tentacle('Alice and Bob went to London.'))  # Should print: Person: Alice, Location: London
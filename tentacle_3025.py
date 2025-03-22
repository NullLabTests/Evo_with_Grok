# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from a given text.

    Args:
    text (str): A string containing the text to be parsed.

    Returns:
    str: A string containing the extracted entities in the format 'Person: <name>, Location: <place>'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Initialize variables to store extracted entities
    person = None
    location = None

    # Split the text into words
    words = text.split()

    # Simple rule-based entity extraction
    for word in words:
        if word.istitle() and word.lower() not in ['the', 'a', 'an', 'to', 'went']:
            if person is None:
                person = word
            else:
                location = word

    # Format the result
    result = f"Person: {person if person else 'None'}, Location: {location if location else 'None'}"
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited New York.'))  # Should print: Person: Mary, Location: York
    print(tentacle('The cat sat on the mat.'))  # Should print: Person: None, Location: None
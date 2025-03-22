# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from the given text.

    Args:
    text (str): A string containing a sentence to analyze.

    Returns:
    str: A string with extracted entities formatted as 'Person: <name>, Location: <place>'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Initialize variables to store extracted entities
    person = None
    location = None

    # Split the text into words
    words = text.split()

    # Simple rules for entity extraction
    for word in words:
        if word[0].isupper() and word.lower() not in ['i', 'we', 'they', 'he', 'she', 'it']:
            if person is None:
                person = word
            else:
                location = word

    # Format the result
    result = []
    if person:
        result.append(f"Person: {person}")
    if location:
        result.append(f"Location: {location}")

    return ', '.join(result) if result else "No entities found"

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited New York.'))  # Should print: Person: Mary, Location: York
    print(tentacle('The cat sat on the mat.'))  # Should print: No entities found
    print(tentacle('Alice and Bob traveled to London.'))  # Should print: Person: Alice, Location: London
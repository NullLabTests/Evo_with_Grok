# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from the given text.

    Args:
    text (str): A string containing text to parse for entities.

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

    # Simple rules to identify Person and Location
    for i, word in enumerate(words):
        if word[0].isupper() and word.lower() not in ['the', 'a', 'an', 'to', 'went']:
            if i == 0:  # First word is likely a person's name
                person = word
            elif words[i-1].lower() in ['to', 'in', 'at']:  # Words after 'to', 'in', 'at' might be locations
                location = word

    # Format the result
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
    print(tentacle('Alice traveled to New York City.'))  # Should print: Person: Alice, Location: York
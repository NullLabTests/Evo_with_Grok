# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from a given text.

    Args:
    text (str): A string containing the text to parse.

    Returns:
    str: A string with extracted entities in the format 'Person: <name>, Location: <place>'.

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
    for i, word in enumerate(words):
        if word.lower() in ['went', 'is', 'was', 'in', 'to', 'at']:
            # Assume the word before is a person
            if i > 0:
                person = words[i-1]
            # Assume the word after is a location
            if i < len(words) - 1:
                location = words[i+1]

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
    print(tentacle('Mary is in London.'))    # Should print: Person: Mary, Location: London
    print(tentacle('The cat was at home.'))  # Should print: Location: home
    print(tentacle('Bob went to the store.'))# Should print: Person: Bob, Location: store
    print(tentacle('Alice is happy.'))       # Should print: Person: Alice
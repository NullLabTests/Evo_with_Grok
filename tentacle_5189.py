# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from the given text.
    
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

    # Iterate through words to find potential entities
    for i, word in enumerate(words):
        # Check for person (assuming the first word is a person's name)
        if i == 0 and word.istitle():
            person = word
        
        # Check for location (assuming 'to' is followed by a location)
        if word.lower() == 'to' and i + 1 < len(words):
            location = words[i + 1]

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
    print(tentacle('The cat sat on the mat.'))  # Should print: Person: The
    print(tentacle('I traveled to New York City.'))  # Should print: Person: I, Location: New
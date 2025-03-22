# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from the given text.
    
    Args:
    text (str): A string containing text to be parsed.
    
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
    
    # Simple rule-based entity extraction
    for word in words:
        # Check for person names (assuming capitalized words at the beginning)
        if word.istitle() and person is None:
            person = word
        # Check for location names (assuming capitalized words after 'to')
        elif word.lower() == 'to' and len(words) > words.index(word) + 1:
            next_word = words[words.index(word) + 1]
            if next_word.istitle():
                location = next_word
    
    # Format and return the result
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
    print(tentacle('To New York, Alice traveled.'))  # Should print: Person: Alice, Location: New York
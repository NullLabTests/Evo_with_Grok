# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.
    
    This function identifies and extracts 'Person' and 'Location' entities from the given text.
    
    Args:
    text (str): A string containing text to be parsed.
    
    Returns:
    str: A string containing the identified entities in the format 'Entity: Value'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Initialize variables to store identified entities
    person = None
    location = None
    
    # Split the text into words
    words = text.split()
    
    # Simple rules for entity identification
    for word in words:
        if word.istitle() and word not in ['To', 'The', 'A', 'An']:
            if person is None:
                person = word
            else:
                location = word
    
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
    print(tentacle('I am going to New York.'))  # Should print: Person: I, Location: York
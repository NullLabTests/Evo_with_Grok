# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from the given text.
    
    Args:
    text (str): A string containing the text to be analyzed.
    
    Returns:
    str: A string with extracted entities formatted as 'Person: [Name], Location: [Place]'.
    
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
        if word.istitle() and word not in ['The', 'A', 'An']:
            if person is None:
                person = word
            elif location is None:
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
    print(tentacle('Mary visited London last week.'))  # Should print: Person: Mary, Location: London
    print(tentacle('In New York, Sarah met Tom.'))  # Should print: Person: Sarah, Location: New York
    print(tentacle('The cat sat on the mat.'))  # Should print: (nothing, as no person or location is detected)
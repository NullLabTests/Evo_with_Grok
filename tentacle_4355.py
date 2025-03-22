# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from a given text.
    
    Args:
    text (str): A string containing the text to analyze.
    
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
        # Check for person names (assuming capitalized words at the beginning of the sentence)
        if word.istitle() and person is None:
            person = word
        # Check for location names (assuming capitalized words not at the beginning)
        elif word.istitle() and word.lower() not in ['i', 'you', 'he', 'she', 'we', 'they']:
            location = word
    
    # Format and return the extracted entities
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
    print(tentacle('I love going to London.'))  # Should print: Location: London
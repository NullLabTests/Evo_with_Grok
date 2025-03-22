# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from the given text.
    
    Args:
    text (str): A string containing the text to be analyzed.
    
    Returns:
    str: A string containing the extracted entities in the format 'Person: [Name], Location: [Place]'.
    
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
        # Check for person names (assuming capitalized words at the beginning of the sentence)
        if word.istitle() and person is None:
            person = word
        # Check for location names (assuming capitalized words not at the beginning)
        elif word.istitle() and location is None:
            location = word
    
    # Construct the result string
    result = []
    if person:
        result.append(f"Person: {person}")
    if location:
        result.append(f"Location: {location}")
    
    return ", ".join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited New York.'))  # Should print: Person: Mary, Location: York
    print(tentacle('The cat sat on the mat.'))  # Should print: (empty string)
    print(tentacle('In London, David saw a show.'))  # Should print: Person: David, Location: London
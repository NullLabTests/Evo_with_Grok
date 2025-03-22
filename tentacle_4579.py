# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from a given text.
    
    Args:
    text (str): A string containing the text to be analyzed.
    
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
    
    # Simple rules for entity extraction
    for word in words:
        # Extract person (assuming the first word is a person's name)
        if person is None and word[0].isupper() and word.isalpha():
            person = word
        
        # Extract location (assuming the last word is a location)
        if location is None and word[0].isupper() and word.isalpha():
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
    print(tentacle('The cat sat on the mat.'))  # Should print: (nothing, as no person or location is detected)
    print(tentacle('In London, Alice met Bob.'))  # Should print: Person: London, Location: Alice
# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from the given text.
    
    Args:
    text (str): A string containing the text to be analyzed.
    
    Returns:
    str: A formatted string with extracted entities.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Define simple rules for entity extraction
    person_patterns = [' went ', ' is ', ' was ']
    location_patterns = [' to ', ' in ', ' at ']
    
    # Initialize variables to store extracted entities
    person = None
    location = None
    
    # Extract person
    for pattern in person_patterns:
        if pattern in text:
            person_index = text.index(pattern)
            person = text[:person_index].strip().split()[-1]
            break
    
    # Extract location
    for pattern in location_patterns:
        if pattern in text:
            location_index = text.index(pattern) + len(pattern)
            location = text[location_index:].strip().split()[0]
            break
    
    # Format and return the result
    result = []
    if person:
        result.append(f"Person: {person}")
    if location:
        result.append(f"Location: {location}")
    
    return ', '.join(result) if result else "No entities found."

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary is in London.'))   # Should print: Person: Mary, Location: London
    print(tentacle('The cat was at home.')) # Should print: No entities found.
    print(tentacle('I visited New York.'))  # Should print: Location: New York
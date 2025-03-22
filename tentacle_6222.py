# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from a given text.

    Args:
    text (str): A string containing the text to parse.

    Returns:
    str: A formatted string with extracted entities.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Initialize dictionaries for entity extraction
    person_keywords = ['went', 'traveled', 'visited']
    location_keywords = ['to', 'in', 'at']
    
    # Split the text into words
    words = text.split()
    
    # Initialize variables to store extracted entities
    person = None
    location = None
    
    # Iterate through words to find entities
    for i, word in enumerate(words):
        if word in person_keywords and i > 0:
            person = words[i-1]
        elif word in location_keywords and i < len(words) - 1:
            location = words[i+1]
    
    # Format and return the result
    result = []
    if person:
        result.append(f"Person: {person}")
    if location:
        result.append(f"Location: {location}")
    
    return ", ".join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary traveled to London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('David visited New York in 2020.'))  # Should print: Person: David, Location: York
    print(tentacle('I went to the store.'))  # Should print: Person: I, Location: store
    print(tentacle('The cat sat on the mat.'))  # Should print: (empty string)
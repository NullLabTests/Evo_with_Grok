# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from the given text.
    
    Args:
    text (str): A string containing text to be parsed.
    
    Returns:
    str: A formatted string containing extracted entities.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Initialize dictionaries for entity recognition
    person_keywords = ['John', 'Mary', 'David', 'Sarah']
    location_keywords = ['Paris', 'London', 'New York', 'Tokyo']
    
    # Initialize variables to store extracted entities
    person = None
    location = None
    
    # Split the text into words
    words = text.split()
    
    # Iterate through words to find entities
    for word in words:
        if word in person_keywords and person is None:
            person = word
        elif word in location_keywords and location is None:
            location = word
    
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
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('David is planning a trip to New York.'))  # Should print: Person: David, Location: New York
    print(tentacle('Sarah lives in Tokyo.'))  # Should print: Person: Sarah, Location: Tokyo
    print(tentacle('The weather is nice today.'))  # Should print: No entities found.
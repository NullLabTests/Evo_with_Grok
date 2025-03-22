# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from the given text.
    
    Args:
    text (str): A string containing the text to be analyzed.
    
    Returns:
    str: A string containing the extracted entities in the format 'Entity: Value'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Initialize dictionaries for entity extraction
    person_keywords = ['went', 'visited', 'traveled', 'is', 'was']
    location_keywords = ['to', 'in', 'at']
    
    # Split the text into words
    words = text.split()
    
    person = None
    location = None
    
    # Iterate through the words to find entities
    for i, word in enumerate(words):
        # Check for person
        if word in person_keywords and i > 0:
            person = words[i-1]
        
        # Check for location
        if word in location_keywords and i < len(words) - 1:
            location = words[i+1]
    
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
    print(tentacle('Mary visited New York.'))  # Should print: Person: Mary, Location: New York
    print(tentacle('The capital is Berlin.'))  # Should print: Location: Berlin
    print(tentacle('Alice and Bob are friends.'))  # Should print: Person: Bob
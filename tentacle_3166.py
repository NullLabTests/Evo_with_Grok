# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to be parsed.
    
    Returns:
    str: A string containing extracted entities in the format 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Define dictionaries for entity recognition
    person_keywords = ['went', 'is', 'was', 'said']
    location_keywords = ['to', 'in', 'at']
    
    # Initialize variables
    person = None
    location = None
    
    # Split the text into words
    words = text.split()
    
    # Iterate through words to find entities
    for i, word in enumerate(words):
        if word in person_keywords and i > 0:
            person = words[i-1]
        elif word in location_keywords and i < len(words) - 1:
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
    print(tentacle('Mary is in London.'))   # Should print: Person: Mary, Location: London
    print(tentacle('The cat sat on the mat.'))  # Should print: (nothing, as no entities are recognized)
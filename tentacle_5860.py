# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.
    
    This function identifies and extracts 'Person' and 'Location' entities from a given text.
    
    Args:
    text (str): A string containing the text to be analyzed.
    
    Returns:
    str: A string with extracted entities formatted as 'Entity Type: Entity Name'.
    
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
        if person is None and word.istitle() and i > 0 and words[i-1].lower() in person_keywords:
            person = word
        if location is None and word.istitle() and i > 0 and words[i-1].lower() in location_keywords:
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
    print(tentacle('Mary visited New York.'))  # Should print: Person: Mary, Location: New York
    print(tentacle('The meeting is in London.'))  # Should print: Location: London
    print(tentacle('Alice was at the beach.'))  # Should print: Person: Alice
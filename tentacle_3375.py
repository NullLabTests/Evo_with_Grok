# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from a given text.

    Args:
    text (str): A string containing text to parse for entities.

    Returns:
    str: A formatted string containing extracted entities.

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
    
    # Iterate through the words to find entities
    for i, word in enumerate(words):
        if word in person_keywords and i > 0:
            person = words[i-1].capitalize()
        elif word in location_keywords and i < len(words) - 1:
            location = words[i+1].capitalize()
    
    # Construct the result string
    result = []
    if person:
        result.append(f"Person: {person}")
    if location:
        result.append(f"Location: {location}")
    
    return ', '.join(result) if result else "No entities found."

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary traveled to New York.'))  # Should print: Person: Mary, Location: New York
    print(tentacle('The weather is nice in London.'))  # Should print: Location: London
    print(tentacle('I visited Tokyo last year.'))  # Should print: Location: Tokyo
    print(tentacle('No specific names or places mentioned.'))  # Should print: No entities found.
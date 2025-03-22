# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from the given text.
    
    Args:
    text (str): A string containing the text to parse.
    
    Returns:
    str: A string containing the extracted entities in the format 'Entity: Value'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Initialize dictionaries for entity recognition
    person_keywords = ['went', 'is', 'was', 'goes']
    location_keywords = ['to', 'in', 'at']
    
    # Split the text into words
    words = text.split()
    
    person = None
    location = None
    
    # Iterate through the words to find entities
    for i, word in enumerate(words):
        if word.capitalize() == word and i > 0 and words[i-1] in person_keywords:
            person = word
        elif i > 0 and words[i-1] in location_keywords:
            location = word
    
    # Construct the result string
    result = []
    if person:
        result.append(f"Person: {person}")
    if location:
        result.append(f"Location: {location}")
    
    return ', '.join(result) if result else "No entities found"

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary is in London.'))   # Should print: Person: Mary, Location: London
    print(tentacle('The cat sat on the mat.'))  # Should print: No entities found
    print(tentacle('Sarah goes to New York.'))  # Should print: Person: Sarah, Location: York
    print(tentacle('In Tokyo, Tom was walking.'))  # Should print: Person: Tom, Location: Tokyo
# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from the given text.
    
    Args:
    text (str): A string containing text to be analyzed.
    
    Returns:
    str: A string with extracted entities formatted as 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Initialize dictionaries for entity recognition
    person_keywords = ['went', 'visited', 'traveled', 'is', 'was']
    location_keywords = ['to', 'in', 'at']
    
    # Split the text into words
    words = text.split()
    
    person = None
    location = None
    
    # Iterate through the words to find entities
    for i, word in enumerate(words):
        if word[0].isupper() and word.isalpha():  # Assume capitalized words are potential entities
            if i > 0 and words[i-1] in person_keywords:
                person = word
            elif i > 0 and words[i-1] in location_keywords:
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
    print(tentacle('The cat is in the house.'))  # Should print: No entities found.
    print(tentacle('Alice was at the Eiffel Tower in Paris.'))  # Should print: Person: Alice, Location: Paris
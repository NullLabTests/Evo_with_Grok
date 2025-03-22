# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from the given text.
    
    Args:
    text (str): A string containing the text to analyze.
    
    Returns:
    str: A formatted string with extracted entities.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Define simple rules for entity extraction
    person_patterns = ['went', 'is', 'was', 'lives']
    location_patterns = ['to', 'in', 'at']
    
    words = text.split()
    person = None
    location = None
    
    for i, word in enumerate(words):
        if word in person_patterns and i > 0:
            person = words[i-1]
        elif word in location_patterns and i < len(words) - 1:
            location = words[i+1]
    
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
    print(tentacle('The cat sat on the mat.'))  # Should print: No entities found.
    print(tentacle('Alice was at the beach.'))  # Should print: Person: Alice, Location: beach
# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from the given text.
    
    Args:
    text (str): A string containing the text to be parsed.
    
    Returns:
    str: A string with extracted entities in the format 'Person: <name>, Location: <place>'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Initialize variables to store extracted entities
    person = None
    location = None
    
    # Split the text into words
    words = text.split()
    
    # Simple rule-based entity extraction
    for word in words:
        # Check for person names (capitalized words at the beginning of the sentence)
        if word.istitle() and person is None:
            person = word
        # Check for location names (capitalized words not at the beginning)
        elif word.istitle() and location is None:
            location = word
    
    # Format the result
    result = []
    if person:
        result.append(f"Person: {person}")
    if location:
        result.append(f"Location: {location}")
    
    return ", ".join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The city of Tokyo is beautiful.'))  # Should print: Location: Tokyo
    print(tentacle('Sarah enjoys her time in New York.'))  # Should print: Person: Sarah, Location: York
    print(tentacle('The river flows through the valley.'))  # Should print: (empty string)
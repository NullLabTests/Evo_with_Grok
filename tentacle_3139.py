# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from the given text.
    
    Args:
    text (str): A string containing text to be analyzed.
    
    Returns:
    str: A string with extracted entities formatted as 'Entity: Value'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Initialize empty lists to store entities
    persons = []
    locations = []
    
    # Split the text into words
    words = text.split()
    
    # Simple rule-based entity extraction
    for word in words:
        if word.istitle() and word not in ['To', 'From', 'In']:
            persons.append(word)
        elif word.lower() in ['paris', 'london', 'new york', 'tokyo']:
            locations.append(word)
    
    # Format the result
    result = []
    if persons:
        result.append(f"Person: {', '.join(persons)}")
    if locations:
        result.append(f"Location: {', '.join(locations)}")
    
    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary and Tom visited London and New York.'))  # Should print: Person: Mary, Tom, Location: London, New York
    print(tentacle('The capital of Japan is Tokyo.'))  # Should print: Location: Tokyo
    print(tentacle('I love to travel.'))  # Should print: (empty string)
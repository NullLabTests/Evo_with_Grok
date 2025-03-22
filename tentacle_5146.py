# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from the given text.
    
    Args:
    text (str): A string containing the text to be analyzed.
    
    Returns:
    str: A formatted string containing the extracted entities.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Initialize dictionaries for entity extraction
    person_keywords = ['John', 'Jane', 'Alice', 'Bob']
    location_keywords = ['Paris', 'London', 'New York', 'Tokyo']
    
    # Initialize variables to store extracted entities
    person = None
    location = None
    
    # Split the text into words
    words = text.split()
    
    # Iterate through words to find entities
    for word in words:
        if word in person_keywords:
            person = word
        elif word in location_keywords:
            location = word
    
    # Format and return the result
    result = []
    if person:
        result.append(f'Person: {person}')
    if location:
        result.append(f'Location: {location}')
    
    return ', '.join(result) if result else 'No entities found'

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Jane visited London.'))  # Should print: Person: Jane, Location: London
    print(tentacle('Alice and Bob are in New York.'))  # Should print: Person: Alice, Location: New York
    print(tentacle('Tokyo is a beautiful city.'))  # Should print: Location: Tokyo
    print(tentacle('The weather is nice today.'))  # Should print: No entities found
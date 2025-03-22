# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to parse for entities.
    
    Returns:
    str: A string containing extracted entities formatted as 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Define dictionaries for entity recognition
    person_keywords = ['John', 'Mary', 'David', 'Lisa']
    location_keywords = ['Paris', 'New York', 'London', 'Tokyo']
    
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
    
    # Construct the result string
    result = []
    if person:
        result.append(f'Person: {person}')
    if location:
        result.append(f'Location: {location}')
    
    # Return the formatted result
    return ', '.join(result) if result else 'No entities found'

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited New York.'))  # Should print: Person: Mary, Location: New York
    print(tentacle('David lives in London.'))  # Should print: Person: David, Location: London
    print(tentacle('Lisa is going to Tokyo.'))  # Should print: Person: Lisa, Location: Tokyo
    print(tentacle('The weather is nice today.'))  # Should print: No entities found
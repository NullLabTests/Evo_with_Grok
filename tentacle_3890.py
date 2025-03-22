# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.
    
    This function identifies and extracts 'Person' and 'Location' entities from a given text.
    It uses simple string matching to identify these entities.
    
    Args:
    text (str): A string containing the text to be parsed.
    
    Returns:
    str: A formatted string containing the identified entities.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Initialize empty lists to store identified entities
    persons = []
    locations = []
    
    # List of common person names (can be expanded)
    person_names = ['John', 'Jane', 'Alice', 'Bob']
    
    # List of common location names (can be expanded)
    location_names = ['Paris', 'London', 'New York', 'Tokyo']
    
    # Split the text into words
    words = text.split()
    
    # Iterate through words to identify entities
    for word in words:
        if word in person_names:
            persons.append(word)
        elif word in location_names:
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
    print(tentacle('Alice visited London and New York.'))  # Should print: Person: Alice, Location: London, New York
    print(tentacle('Bob is in Tokyo.'))  # Should print: Person: Bob, Location: Tokyo
    print(tentacle('Jane likes to travel.'))  # Should print: Person: Jane
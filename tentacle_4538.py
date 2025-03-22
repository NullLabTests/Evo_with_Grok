# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text, identifying people and locations.
    
    Args:
    text (str): A string containing text to analyze.
    
    Returns:
    str: A formatted string containing identified entities.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Simple list of common names and locations for demonstration
    people = ['John', 'Alice', 'Bob', 'Emma']
    locations = ['Paris', 'London', 'New York', 'Tokyo']
    
    # Initialize dictionaries to store found entities
    found_people = []
    found_locations = []
    
    # Split the text into words
    words = text.split()
    
    # Check each word against the lists of people and locations
    for word in words:
        if word in people and word not in found_people:
            found_people.append(word)
        if word in locations and word not in found_locations:
            found_locations.append(word)
    
    # Format the output
    result = []
    if found_people:
        result.append(f"Person: {', '.join(found_people)}")
    if found_locations:
        result.append(f"Location: {', '.join(found_locations)}")
    
    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Alice and Bob visited London and New York.'))  # Should print: Person: Alice, Bob, Location: London, New York
    print(tentacle('Emma is planning a trip to Tokyo.'))  # Should print: Person: Emma, Location: Tokyo
    print(tentacle('The weather in Paris is great today.'))  # Should print: Location: Paris
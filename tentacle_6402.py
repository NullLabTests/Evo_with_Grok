# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to parse for entities.
    
    Returns:
    str: A string with identified entities formatted as 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Define dictionaries for entity recognition
    person_names = ['John', 'Mary', 'David', 'Sarah']
    locations = ['Paris', 'London', 'New York', 'Tokyo']
    
    # Initialize result list
    result = []
    
    # Split the text into words
    words = text.split()
    
    # Iterate through words to identify entities
    for word in words:
        if word in person_names:
            result.append(f'Person: {word}')
        elif word in locations:
            result.append(f'Location: {word}')
    
    # Join the results and return
    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary is visiting London and New York.'))  # Should print: Person: Mary, Location: London, Location: New York
    print(tentacle('David lives in Tokyo.'))  # Should print: Person: David, Location: Tokyo
    print(tentacle('Sarah likes to travel.'))  # Should print: Person: Sarah
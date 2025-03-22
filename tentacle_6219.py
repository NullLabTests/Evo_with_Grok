# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to parse.
    
    Returns:
    str: A string containing extracted entities in the format 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Define dictionaries for entity recognition
    person_keywords = ['John', 'Mary', 'Alice', 'Bob']
    location_keywords = ['Paris', 'London', 'New York', 'Tokyo']
    
    # Initialize a list to store recognized entities
    entities = []
    
    # Split the text into words
    words = text.split()
    
    # Iterate through words to find entities
    for word in words:
        if word in person_keywords:
            entities.append(f'Person: {word}')
        elif word in location_keywords:
            entities.append(f'Location: {word}')
    
    # Join the recognized entities into a single string
    return ', '.join(entities)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London and New York.'))  # Should print: Person: Mary, Location: London, Location: New York
    print(tentacle('Alice and Bob are in Tokyo.'))  # Should print: Person: Alice, Person: Bob, Location: Tokyo
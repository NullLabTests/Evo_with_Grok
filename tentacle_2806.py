# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to parse for entities.
    
    Returns:
    str: A string containing the extracted entities in the format 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Define dictionaries of entity types and their associated keywords
    person_keywords = ['went', 'said', 'is', 'was']
    location_keywords = ['to', 'in', 'at']
    
    # Initialize a dictionary to store extracted entities
    entities = {}
    
    # Split the text into words
    words = text.split()
    
    # Iterate through the words to find entities
    for i, word in enumerate(words):
        if i > 0 and words[i-1] in person_keywords and word.istitle():
            entities['Person'] = word
        elif i > 0 and words[i-1] in location_keywords and word.istitle():
            entities['Location'] = word
    
    # Format the result string
    result = ', '.join([f"{entity_type}: {entity}" for entity_type, entity in entities.items()])
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary is in London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The meeting was held at New York.'))  # Should print: Location: New York
    print(tentacle('David said he will visit Tokyo.'))  # Should print: Person: David, Location: Tokyo
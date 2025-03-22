# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to parse.
    
    Returns:
    str: A string with extracted entities formatted as 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Initialize a dictionary to store entities
    entities = {}
    
    # Define lists of entity types and their associated keywords
    person_keywords = ['went', 'is', 'was', 'said']
    location_keywords = ['to', 'in', 'at']
    
    # Split the text into words
    words = text.split()
    
    # Iterate through the words to identify entities
    for i, word in enumerate(words):
        # Check for person entity
        if i > 0 and words[i-1] in person_keywords and word.istitle():
            entities['Person'] = word
        
        # Check for location entity
        if i < len(words) - 1 and words[i+1] in location_keywords and word.istitle():
            entities['Location'] = word
    
    # Format the result
    result = ', '.join([f"{entity_type}: {entity}" for entity_type, entity in entities.items()])
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary is in London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The meeting was at New York.'))  # Should print: Location: New York
    print(tentacle('David said he lives in Tokyo.'))  # Should print: Person: David, Location: Tokyo
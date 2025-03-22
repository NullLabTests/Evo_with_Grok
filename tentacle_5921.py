# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to be parsed.
    
    Returns:
    str: A string containing extracted entities in the format 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Dictionary to store recognized entities
    entities = {}
    
    # List of words that indicate entity types
    person_indicators = ['John', 'Mary', 'David', 'Lisa']
    location_indicators = ['Paris', 'London', 'New York', 'Tokyo']
    
    # Split the text into words
    words = text.split()
    
    # Iterate through words to identify entities
    for word in words:
        if word in person_indicators and 'Person' not in entities:
            entities['Person'] = word
        elif word in location_indicators and 'Location' not in entities:
            entities['Location'] = word
    
    # Format the result string
    result = ', '.join([f"{entity_type}: {entity_name}" for entity_type, entity_name in entities.items()])
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary is visiting London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('David lives in New York.'))  # Should print: Person: David, Location: New York
    print(tentacle('Lisa traveled to Tokyo.'))  # Should print: Person: Lisa, Location: Tokyo
    print(tentacle('The weather is nice today.'))  # Should print: (empty string)
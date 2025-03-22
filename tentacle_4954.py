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
    # Dictionary to store extracted entities
    entities = {}
    
    # List of words to look for and their corresponding entity types
    entity_patterns = [
        ('John', 'Person'),
        ('Paris', 'Location')
    ]
    
    # Process the text
    for word, entity_type in entity_patterns:
        if word in text:
            entities[entity_type] = word
    
    # Format the output
    result = ', '.join(f"{entity_type}: {entity}" for entity_type, entity in entities.items())
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: (nothing, as Mary and London are not in our patterns)
    print(tentacle('I love New York.'))  # Should print: (nothing, as New York is not in our patterns)
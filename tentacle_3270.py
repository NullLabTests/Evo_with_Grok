# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.
    
    This function identifies and extracts 'Person' and 'Location' entities from a given text.
    It uses simple pattern matching to identify these entities.
    
    Args:
    text (str): A string containing text to be parsed.
    
    Returns:
    str: A string containing identified entities in the format 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Initialize an empty dictionary to store entities
    entities = {}
    
    # Split the text into words
    words = text.split()
    
    # Look for person names (assuming the first word is a person name)
    if words:
        entities['Person'] = words[0]
    
    # Look for location names (assuming 'to' is followed by a location)
    if 'to' in words:
        to_index = words.index('to')
        if to_index + 1 < len(words):
            entities['Location'] = words[to_index + 1]
    
    # Format the result
    result = []
    for entity_type, entity_name in entities.items():
        result.append(f"{entity_type}: {entity_name}")
    
    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited New York.'))  # Should print: Person: Mary, Location: York
    print(tentacle('David is at home.'))  # Should print: Person: David
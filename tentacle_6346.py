# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from the given text.
    
    Args:
    text (str): A string containing the text to parse.
    
    Returns:
    str: A string with extracted entities formatted as 'Entity: Value'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Dictionary to store extracted entities
    entities = {}
    
    # Split the text into words
    words = text.split()
    
    # Extract Person (assuming the first word is a person's name)
    if words:
        entities['Person'] = words[0]
    
    # Extract Location (assuming 'to' is followed by a location)
    if 'to' in words:
        to_index = words.index('to')
        if to_index + 1 < len(words):
            entities['Location'] = words[to_index + 1]
    
    # Format the result
    result = ', '.join([f"{entity}: {value}" for entity, value in entities.items()])
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Alice visited New York.'))  # Should print: Person: Alice, Location: York
    print(tentacle('Bob is in London.'))  # Should print: Person: Bob
    print(tentacle('Mary likes to travel.'))  # Should print: Person: Mary
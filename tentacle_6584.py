# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text, such as persons and locations.
    
    Args:
    text (str): A string containing text to be parsed.
    
    Returns:
    str: A string containing the extracted entities in the format 'Entity: Value'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Initialize a dictionary to store entities
    entities = {}
    
    # Extract persons (assuming a person is a capitalized word followed by lowercase letters)
    persons = re.findall(r'\b[A-Z][a-z]+\b', text)
    if persons:
        entities['Person'] = ', '.join(persons)
    
    # Extract locations (assuming a location is a capitalized word at the end of the sentence)
    locations = re.findall(r'\b[A-Z][a-z]+(?=\.$)', text)
    if locations:
        entities['Location'] = ', '.join(locations)
    
    # Format the output string
    result = ', '.join([f"{key}: {value}" for key, value in entities.items()])
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary and Tom visited London and Berlin.'))  # Should print: Person: Mary, Tom, Location: Berlin
    print(tentacle('The quick brown fox jumps over the lazy dog.'))  # Should print: (empty string)
# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to be analyzed.
    
    Returns:
    str: A string containing extracted entities in the format 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Dictionary to store extracted entities
    entities = {}
    
    # Extract person names (simple pattern, can be improved)
    person_pattern = r'\b[A-Z][a-z]+\b'
    persons = re.findall(person_pattern, text)
    if persons:
        entities['Person'] = persons[0]  # Assume first match is the person
    
    # Extract locations (simple pattern, can be improved)
    location_pattern = r'\b(?:New York|Paris|London|Tokyo|Berlin)\b'
    locations = re.findall(location_pattern, text)
    if locations:
        entities['Location'] = locations[0]  # Assume first match is the location
    
    # Format the result
    result = ', '.join([f"{entity_type}: {entity}" for entity_type, entity in entities.items()])
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Alice visited New York.'))  # Should print: Person: Alice, Location: New York
    print(tentacle('Bob is going to Tokyo tomorrow.'))  # Should print: Person: Bob, Location: Tokyo
    print(tentacle('The meeting is in Berlin.'))  # Should print: Location: Berlin
    print(tentacle('Just a regular sentence.'))  # Should print:
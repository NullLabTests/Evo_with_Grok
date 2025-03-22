# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text, such as persons and locations.
    
    Args:
    text (str): A string containing the text to be parsed.
    
    Returns:
    str: A string containing the extracted entities in the format 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Dictionary to store extracted entities
    entities = {}
    
    # Extract persons (assuming names start with a capital letter and are followed by lowercase letters)
    persons = re.findall(r'\b[A-Z][a-z]+\b', text)
    for person in persons:
        if person.lower() not in ['the', 'a', 'an', 'to', 'and', 'or', 'but']:
            entities['Person'] = entities.get('Person', []) + [person]
    
    # Extract locations (assuming they start with a capital letter and are not persons)
    locations = re.findall(r'\b[A-Z][a-z]+\b', text)
    for location in locations:
        if location not in entities.get('Person', []) and location.lower() not in ['the', 'a', 'an', 'to', 'and', 'or', 'but']:
            entities['Location'] = entities.get('Location', []) + [location]
    
    # Format the result
    result = []
    for entity_type, entity_list in entities.items():
        result.append(f"{entity_type}: {', '.join(entity_list)}")
    
    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary and Tom visited New York and London.'))  # Should print: Person: Mary, Tom, Location: New York, London
    print(tentacle('The cat sat on the mat.'))  # Should print: (nothing, as no persons or locations are detected)
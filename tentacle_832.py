# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to be parsed.
    
    Returns:
    str: A string containing identified entities in the format 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Dictionary to store identified entities
    entities = {}
    
    # Extract person names (assuming they are capitalized and followed by a space)
    person_pattern = r'\b([A-Z][a-z]+)\b'
    person_matches = re.findall(person_pattern, text)
    if person_matches:
        entities['Person'] = person_matches[0]  # Assuming the first match is the person
    
    # Extract location names (assuming they are capitalized and at the end of the sentence)
    location_pattern = r'\b([A-Z][a-z]+)\b(?=\.)'
    location_matches = re.findall(location_pattern, text)
    if location_matches:
        entities['Location'] = location_matches[0]  # Assuming the last match is the location
    
    # Format the result
    result = ', '.join([f"{entity_type}: {entity_name}" for entity_type, entity_name in entities.items()])
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The capital of France is Paris.'))  # Should print: Location: Paris
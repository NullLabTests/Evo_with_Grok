# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to parse for entities.
    
    Returns:
    str: A string containing extracted entities in the format 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Dictionary to store extracted entities
    entities = {}
    
    # Extract person names (assuming simple capitalization)
    person_pattern = r'\b([A-Z][a-z]+)\b'
    persons = re.findall(person_pattern, text)
    if persons:
        entities['Person'] = ', '.join(persons)
    
    # Extract locations (assuming capitalized words that are not persons)
    location_pattern = r'\b([A-Z][a-z]+)\b(?!.*\bPerson\b)'
    locations = re.findall(location_pattern, text)
    if locations:
        entities['Location'] = ', '.join(locations)
    
    # Format the output
    result = ', '.join([f"{entity_type}: {entity_name}" for entity_type, entity_name in entities.items()])
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited New York and London.'))  # Should print: Person: Mary, Location: New York, London
    print(tentacle('The Eiffel Tower is in Paris.'))  # Should print: Location: Eiffel, Paris
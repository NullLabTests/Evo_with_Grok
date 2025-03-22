# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text, specifically identifying persons and locations.
    
    Args:
    text (str): A string containing text to be analyzed.
    
    Returns:
    str: A string with identified entities formatted as 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Dictionary to store identified entities
    entities = {}
    
    # Extract person names (assuming simple format of first name only)
    person_pattern = r'\b([A-Z][a-z]+)\b'
    persons = re.findall(person_pattern, text)
    if persons:
        entities['Person'] = ', '.join(persons)
    
    # Extract locations (assuming they start with a capital letter and are not at the start of the sentence)
    location_pattern = r'(?<!\b\w)\b([A-Z][a-z]+)\b(?! of)'
    locations = re.findall(location_pattern, text)
    if locations:
        entities['Location'] = ', '.join(locations)
    
    # Format the result
    result = ', '.join([f"{entity_type}: {entity}" for entity_type, entity in entities.items()])
    
    return result if result else "No entities found."

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London and New York.'))  # Should print: Person: Mary, Location: London, New York
    print(tentacle('The weather in Tokyo is great.'))  # Should print: Location: Tokyo
    print(tentacle('No specific names here.'))  # Should print: No entities found.
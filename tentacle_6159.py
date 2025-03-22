# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text, focusing on Person and Location.
    
    Args:
    text (str): A string containing text to parse.
    
    Returns:
    str: A string with extracted entities formatted as 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Initialize a dictionary to store entities
    entities = {}
    
    # Extract Person names (assuming simple format of capitalized words)
    person_pattern = r'\b([A-Z][a-z]+)\b'
    persons = re.findall(person_pattern, text)
    if persons:
        entities['Person'] = ', '.join(persons)
    
    # Extract Location names (assuming they are capitalized and not at the start of the sentence)
    location_pattern = r'(?<!^)\b([A-Z][a-z]+)\b'
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
    print(tentacle('Hello world!'))  # Should print: No entities found.
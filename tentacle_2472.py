# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing the text to parse.
    
    Returns:
    str: A string containing the extracted entities in the format 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Dictionary to store extracted entities
    entities = {}
    
    # Extract person names (simple regex, assumes first word is a name)
    person_match = re.match(r'^([A-Z][a-z]+)\b', text)
    if person_match:
        entities['Person'] = person_match.group(1)
    
    # Extract location names (simple regex, assumes last word is a location)
    location_match = re.search(r'\b([A-Z][a-z]+)\.$', text)
    if location_match:
        entities['Location'] = location_match.group(1)
    
    # Format the result
    result = ', '.join(f"{entity_type}: {entity_name}" for entity_type, entity_name in entities.items())
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Alice visited London.'))  # Should print: Person: Alice, Location: London
    print(tentacle('The Eiffel Tower is in Paris.'))  # Should print: Location: Paris
    print(tentacle('Bob likes to travel.'))  # Should print: Person: Bob
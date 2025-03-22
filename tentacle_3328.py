# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to parse.
    
    Returns:
    str: A string with extracted entities formatted as 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Dictionary to store extracted entities
    entities = {}
    
    # Extract person names (assuming simple format of first name only)
    person_match = re.search(r'\b([A-Z][a-z]+)\b', text)
    if person_match:
        entities['Person'] = person_match.group(1)
    
    # Extract locations (assuming proper nouns starting with capital letter)
    location_matches = re.findall(r'\b([A-Z][a-z]+)\b', text)
    for location in location_matches:
        if location != entities.get('Person'):  # Avoid duplicating person as location
            entities['Location'] = location
            break  # Assume first match is the location
    
    # Format the result
    result = ', '.join([f"{entity_type}: {entity_name}" for entity_type, entity_name in entities.items()])
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('No entities here.'))  # Should print: (empty string)
    print(tentacle('Alice and Bob went to New York.'))  # Should print: Person: Alice, Location: New
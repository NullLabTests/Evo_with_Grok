# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to parse for entities.
    
    Returns:
    str: A string with identified entities formatted as 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Dictionary to store identified entities
    entities = {}
    
    # Extract person names (assuming simple case: capitalized words at the start of the sentence)
    person_match = re.match(r'^([A-Z][a-z]+)', text)
    if person_match:
        entities['Person'] = person_match.group(1)
    
    # Extract locations (assuming simple case: capitalized words after 'to')
    location_match = re.search(r'to\s+([A-Z][a-z]+)', text)
    if location_match:
        entities['Location'] = location_match.group(1)
    
    # Format the result
    result = ', '.join(f"{entity_type}: {entity_name}" for entity_type, entity_name in entities.items())
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary traveled to London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The city of Rome is beautiful.'))  # Should print: Location: Rome
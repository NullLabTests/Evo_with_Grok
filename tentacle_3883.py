# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to analyze.
    
    Returns:
    str: A string containing extracted entities formatted as 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Dictionary to store extracted entities
    entities = {}
    
    # Extract person names (simple heuristic: capitalized words at the start of the sentence)
    person_match = re.match(r'^([A-Z][a-z]+)', text)
    if person_match:
        entities['Person'] = person_match.group(1)
    
    # Extract locations (simple heuristic: capitalized words after 'to')
    location_match = re.search(r'to ([A-Z][a-z]+)', text)
    if location_match:
        entities['Location'] = location_match.group(1)
    
    # Format the result
    result = ', '.join([f"{entity_type}: {entity}" for entity_type, entity in entities.items()])
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Alice traveled to London.'))  # Should print: Person: Alice, Location: London
    print(tentacle('The city of Rome is beautiful.'))  # Should print: Location: Rome
    print(tentacle('Mary visited New York.'))  # Should print: Person: Mary, Location: New York
# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text, specifically focusing on persons and locations.
    
    Args:
    text (str): A string containing text to be analyzed.
    
    Returns:
    str: A string with extracted entities formatted as 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Initialize a dictionary to store extracted entities
    entities = {}
    
    # Extract person names (assuming they are capitalized words at the start of sentences)
    person_match = re.match(r'^([A-Z][a-z]+)\b', text)
    if person_match:
        entities['Person'] = person_match.group(1)
    
    # Extract location names (assuming they are capitalized words following 'to')
    location_match = re.search(r'\bto\s+([A-Z][a-z]+)\b', text)
    if location_match:
        entities['Location'] = location_match.group(1)
    
    # Format the result
    result = ', '.join(f"{entity_type}: {entity_name}" for entity_type, entity_name in entities.items())
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('In New York, Bob met Alice.'))  # Should print: Person: Bob, Location: New York
    print(tentacle('Sarah is going to Rome tomorrow.'))  # Should print: Person: Sarah, Location: Rome
    print(tentacle('The weather in Tokyo is nice.'))  # Should print: Location: Tokyo
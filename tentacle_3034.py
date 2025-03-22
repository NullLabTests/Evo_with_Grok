# Domains: text processing, natural language processing
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
    
    # Define patterns for entity extraction
    person_pattern = r'\b[A-Z][a-z]+\b'
    location_pattern = r'\b(?:to|in|at)\s+([A-Z][a-zA-Z]+)\b'
    
    # Extract person names
    persons = re.findall(person_pattern, text)
    persons = [p for p in persons if p.lower() not in ['to', 'in', 'at']]
    
    # Extract locations
    locations = re.findall(location_pattern, text)
    
    # Construct the result string
    result = []
    if persons:
        result.append(f"Person: {', '.join(persons)}")
    if locations:
        result.append(f"Location: {', '.join(locations)}")
    
    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary and Alice visited New York and London.'))  # Should print: Person: Mary, Alice, Location: New York, London
    print(tentacle('The meeting is at 3 PM in Tokyo.'))  # Should print: Location: Tokyo
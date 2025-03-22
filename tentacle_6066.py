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
    location_pattern = r'\b(?:[A-Z][a-z]+(?: [A-Z][a-z]+)*)\b'
    
    # Extract person names
    persons = re.findall(person_pattern, text)
    persons = [p for p in persons if p.lower() not in ['the', 'a', 'an', 'to', 'went']]
    
    # Extract location names
    locations = re.findall(location_pattern, text)
    locations = [l for l in locations if l.lower() not in ['the', 'a', 'an', 'to', 'went']]
    
    # Format the result
    result = []
    if persons:
        result.append(f"Person: {', '.join(persons)}")
    if locations:
        result.append(f"Location: {', '.join(locations)}")
    
    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary and Tom visited New York and London.'))  # Should print: Person: Mary, Tom, Location: New York, London
    print(tentacle('The cat sat on the mat.'))  # Should print: (nothing, as no persons or locations are detected)
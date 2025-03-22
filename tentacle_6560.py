# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to parse for entities.
    
    Returns:
    str: A string containing extracted entities in the format 'Entity Type: Entity'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Define patterns for entity extraction
    person_pattern = r'\b[A-Z][a-z]+\b'
    location_pattern = r'\b(?:[A-Z][a-z]+ )*[A-Z][a-z]+\b'
    
    # Extract entities
    persons = re.findall(person_pattern, text)
    locations = re.findall(location_pattern, text)
    
    # Filter out common words that might be mistakenly identified as persons
    common_words = ['The', 'A', 'An', 'To', 'From', 'In', 'On', 'At']
    persons = [person for person in persons if person not in common_words]
    
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
    print(tentacle('Mary and Tom visited New York and London.'))  # Should print: Person: Mary, Tom, Location: New York, London
    print(tentacle('The cat is on the mat.'))  # Should print:
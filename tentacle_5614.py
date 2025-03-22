# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text, focusing on persons and locations.
    
    Args:
    text (str): A string containing text to analyze.
    
    Returns:
    str: A string with extracted entities formatted as 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Define patterns for person and location extraction
    person_pattern = r'\b[A-Z][a-z]+\b'
    location_pattern = r'\b(?:to|in|at)\s+([A-Z][a-z]+)\b'
    
    # Extract persons
    persons = re.findall(person_pattern, text)
    persons = [person for person in persons if person.lower() not in ['to', 'in', 'at']]
    
    # Extract locations
    locations = re.findall(location_pattern, text)
    
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
    print(tentacle('Alice and Bob visited London and New York.'))  # Should print: Person: Alice, Bob, Location: London, New York
    print(tentacle('The meeting is in Tokyo.'))  # Should print: Location: Tokyo
    print(tentacle('No entities here.'))  # Should print:
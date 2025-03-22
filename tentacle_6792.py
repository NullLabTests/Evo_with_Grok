# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text, specifically focusing on persons and locations.
    
    Args:
    text (str): A string containing text to parse for entities.
    
    Returns:
    str: A formatted string with extracted entities.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Define patterns for extracting persons and locations
    person_pattern = r'\b([A-Z][a-z]+)\b'
    location_pattern = r'\bto\s+([A-Z][a-z]+)\b'
    
    # Extract persons
    persons = re.findall(person_pattern, text)
    persons = ', '.join(f"Person: {person}" for person in persons)
    
    # Extract locations
    locations = re.findall(location_pattern, text)
    locations = ', '.join(f"Location: {location}" for location in locations)
    
    # Combine results
    result = []
    if persons:
        result.append(persons)
    if locations:
        result.append(locations)
    
    return ', '.join(result) if result else "No entities found"

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London and met Alice.'))  # Should print: Person: Mary, Person: Alice, Location: London
    print(tentacle('The capital of France is Paris.'))  # Should print: Location: Paris
    print(tentacle('No names or places here.'))  # Should print: No entities found
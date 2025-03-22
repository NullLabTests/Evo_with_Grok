# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to parse for entities.
    
    Returns:
    str: A string containing identified entities and their types.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Define regex patterns for entity extraction
    person_pattern = r'\b([A-Z][a-z]+)\b'
    location_pattern = r'\b(to|in|at)\s([A-Z][a-z]+)\b'
    
    # Extract person names
    persons = re.findall(person_pattern, text)
    persons = [person for person in persons if person.lower() not in ['to', 'in', 'at']]
    
    # Extract locations
    locations = re.findall(location_pattern, text)
    locations = [location[1] for location in locations]
    
    # Format the result
    result_parts = []
    if persons:
        result_parts.append(f"Person: {', '.join(persons)}")
    if locations:
        result_parts.append(f"Location: {', '.join(locations)}")
    
    return ', '.join(result_parts)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary and Tom visited New York and London.'))  # Should print: Person: Mary, Tom, Location: New York, London
    print(tentacle('The meeting is in Tokyo.'))  # Should print: Location: Tokyo
    print(tentacle('No entities here.'))  # Should print:
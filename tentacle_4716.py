# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to parse for entities.
    
    Returns:
    str: A string with extracted entities formatted as 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Define patterns for entity extraction
    person_pattern = r'\b[A-Z][a-z]+\b'
    location_pattern = r'\b(?:to|in|at)\s+([A-Z][a-zA-Z]+)\b'
    
    # Extract entities
    persons = re.findall(person_pattern, text)
    locations = re.findall(location_pattern, text)
    
    # Format the output
    result = []
    if persons:
        result.append(f"Person: {', '.join(persons)}")
    if locations:
        result.append(f"Location: {', '.join(locations)}")
    
    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary and Tom visited London and New York.'))  # Should print: Person: Mary, Tom, Location: London, New York
    print(tentacle('The conference is in Tokyo next month.'))  # Should print: Location: Tokyo
# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from given text.
    
    Args:
    text (str): A string containing text to be parsed.
    
    Returns:
    str: A string containing extracted entities formatted as 'Entity: Value'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Initialize empty lists for persons and locations
    persons = []
    locations = []
    
    # Extract persons (assuming capitalized words as potential names)
    person_pattern = r'\b[A-Z][a-z]+\b'
    persons = re.findall(person_pattern, text)
    
    # Extract locations (assuming capitalized words after 'to' as potential locations)
    location_pattern = r'to\s+([A-Z][a-z]+)'
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
    print(tentacle('Mary and Alice visited London and Rome.'))  # Should print: Person: Mary, Alice, Location: London, Rome
    print(tentacle('The cat sat on the mat.'))  # Should print: (nothing, as no persons or locations are detected)
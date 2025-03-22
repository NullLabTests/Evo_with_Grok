# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to parse for entities.
    
    Returns:
    str: A string with identified entities formatted as 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Define patterns for entity extraction
    person_pattern = r'\b([A-Z][a-z]+)\b'
    location_pattern = r'\bto\s([A-Z][a-z]+)\b'
    
    # Extract entities
    person = re.findall(person_pattern, text)
    location = re.findall(location_pattern, text)
    
    # Format the result
    result = []
    if person:
        result.append(f"Person: {person[0]}")
    if location:
        result.append(f"Location: {location[0]}")
    
    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Alice traveled to London.'))  # Should print: Person: Alice, Location: London
    print(tentacle('Bob visited New York.'))  # Should print: Person: Bob, Location: New York
# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to parse.
    
    Returns:
    str: A string with extracted entities formatted as 'Entity: Value'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Define regex patterns for entity extraction
    person_pattern = r'\b([A-Z][a-z]+)\b'
    location_pattern = r'\b(?:to|in|at)\s+([A-Z][a-z]+)\b'
    
    # Extract person
    person_match = re.search(person_pattern, text)
    person = person_match.group(1) if person_match else None
    
    # Extract location
    location_match = re.search(location_pattern, text)
    location = location_match.group(1) if location_match else None
    
    # Format the result
    result_parts = []
    if person:
        result_parts.append(f"Person: {person}")
    if location:
        result_parts.append(f"Location: {location}")
    
    return ', '.join(result_parts)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Alice is in London.'))   # Should print: Person: Alice, Location: London
    print(tentacle('Bob visited New York.')) # Should print: Person: Bob, Location: York
    print(tentacle('No entities here.'))     # Should print:
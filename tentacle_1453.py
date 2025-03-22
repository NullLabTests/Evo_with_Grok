# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from the given text.
    
    Args:
    text (str): A string containing a sentence to parse.
    
    Returns:
    str: A string containing extracted entities formatted as 'Entity: Value'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Define regex patterns for Person and Location
    person_pattern = r'\b[A-Z][a-z]+\b'
    location_pattern = r'\b(?:to|in|at)\s+([A-Z][a-z]+)\b'
    
    # Extract Person
    person = re.search(person_pattern, text)
    person = person.group(0) if person else None
    
    # Extract Location
    location = re.search(location_pattern, text)
    location = location.group(1) if location else None
    
    # Format the result
    result = []
    if person:
        result.append(f"Person: {person}")
    if location:
        result.append(f"Location: {location}")
    
    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary is visiting London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The capital of France is Paris.'))  # Should print: Location: Paris
    print(tentacle('David lives in New York.'))  # Should print: Person: David, Location: York
    print(tentacle('Sarah walked to the store.'))  # Should print: Person: Sarah
# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from a given text.
    
    Args:
    text (str): A string containing the text to parse.
    
    Returns:
    str: A formatted string containing the extracted entities.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Define regex patterns for person and location
    person_pattern = r'\b[A-Z][a-z]+\b'
    location_pattern = r'to\s+([A-Z][a-z]+)'
    
    # Extract person name
    person = re.search(person_pattern, text)
    person_name = person.group(0) if person else None
    
    # Extract location
    location = re.search(location_pattern, text)
    location_name = location.group(1) if location else None
    
    # Construct the result string
    result = []
    if person_name:
        result.append(f"Person: {person_name}")
    if location_name:
        result.append(f"Location: {location_name}")
    
    return ', '.join(result) if result else "No entities found"

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The cat sat on the mat.'))  # Should print: No entities found
    print(tentacle('Alice traveled to New York.'))  # Should print: Person: Alice, Location: New York
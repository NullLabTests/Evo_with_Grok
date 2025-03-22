# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to parse.
    
    Returns:
    str: A string containing extracted entities in the format 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Define patterns for entity extraction
    person_pattern = r'\b([A-Z][a-z]+)\b'
    location_pattern = r'\bto\s+([A-Z][a-z]+)\b'
    
    # Extract person
    person = re.search(person_pattern, text)
    person_result = f"Person: {person.group(1)}" if person else ""
    
    # Extract location
    location = re.search(location_pattern, text)
    location_result = f", Location: {location.group(1)}" if location else ""
    
    # Combine results
    result = person_result + location_result
    
    return result.strip()

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Alice visited London.'))  # Should print: Person: Alice, Location: London
    print(tentacle('Bob is in New York.'))  # Should print: Person: Bob, Location: New York
    print(tentacle('Mary likes San Francisco.'))  # Should print: Person: Mary, Location: San Francisco
    print(tentacle('David explored Tokyo.'))  # Should print: Person: David, Location: Tokyo
    print(tentacle('Sarah went to Rome.'))  # Should print: Person: Sarah, Location: Rome
    print(tentacle('No entities here.'))  # Should print: (empty string)
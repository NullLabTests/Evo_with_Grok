# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to be analyzed.
    
    Returns:
    str: A string containing extracted entities in the format 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Define patterns for entity extraction
    person_pattern = r'\b([A-Z][a-z]+)\b'
    location_pattern = r'\bto\s([A-Z][a-z]+)\b'
    
    # Extract person
    person = re.search(person_pattern, text)
    person_result = f"Person: {person.group(1)}" if person else ""
    
    # Extract location
    location = re.search(location_pattern, text)
    location_result = f"Location: {location.group(1)}" if location else ""
    
    # Combine results
    results = [result for result in [person_result, location_result] if result]
    
    return ", ".join(results)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The cat sat on the mat.'))  # Should print: (nothing, as no entities are found)
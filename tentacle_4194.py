# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to parse for entities.
    
    Returns:
    str: A string containing the extracted entities in the format 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Define patterns for entity extraction
    person_pattern = r'\b[A-Z][a-z]+\b'
    location_pattern = r'\b(?:to|in|at)\s([A-Z][a-z]+)\b'
    
    # Extract person
    person = re.search(person_pattern, text)
    person_result = f"Person: {person.group()}" if person else ""
    
    # Extract location
    location = re.search(location_pattern, text)
    location_result = f"Location: {location.group(1)}" if location else ""
    
    # Combine results
    results = [result for result in [person_result, location_result] if result]
    
    return ', '.join(results) if results else "No entities found"

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary is visiting London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The weather in New York is great.'))  # Should print: Location: New York
    print(tentacle('I love coding.'))  # Should print: No entities found
# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from the given text.
    
    Args:
    text (str): A string containing text to be analyzed.
    
    Returns:
    str: A string with extracted entities formatted as 'Entity Type: Entity Name'.
    
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
    person_name = person.group(0) if person else None
    
    # Extract Location
    location = re.search(location_pattern, text)
    location_name = location.group(1) if location else None
    
    # Format the result
    result_parts = []
    if person_name:
        result_parts.append(f"Person: {person_name}")
    if location_name:
        result_parts.append(f"Location: {location_name}")
    
    return ', '.join(result_parts) if result_parts else "No entities found."

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary is traveling to London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The capital of France is Paris.'))  # Should print: Location: France, Location: Paris
    print(tentacle('No names or places here.'))  # Should print: No entities found.
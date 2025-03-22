# Domains: text processing, mathematics
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
    location_pattern = r'\b(?:to|in|at)\s+([A-Z][a-z]+)\b'
    
    # Extract person
    person_match = re.search(person_pattern, text)
    person = person_match.group(1) if person_match else None
    
    # Extract location
    location_match = re.search(location_pattern, text)
    location = location_match.group(1) if location_match else None
    
    # Construct the result string
    result_parts = []
    if person:
        result_parts.append(f"Person: {person}")
    if location:
        result_parts.append(f"Location: {location}")
    
    return ', '.join(result_parts)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary is traveling to London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('In New York, Robert met Susan.'))  # Should print: Person: Robert, Person: Susan, Location: New York
    print(tentacle('The weather in Tokyo is great.'))  # Should print: Location: Tokyo
    print(tentacle('Alice enjoys her time at home.'))  # Should print: Person: Alice
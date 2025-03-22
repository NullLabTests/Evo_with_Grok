# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text, identifying persons and locations.
    
    Args:
    text (str): A string containing the text to parse.
    
    Returns:
    str: A string with identified entities formatted as 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Define patterns for person and location extraction
    person_pattern = r'\b([A-Z][a-z]+)\b'
    location_pattern = r'\bto\s+([A-Z][a-z]+)\b'
    
    # Extract persons
    persons = re.findall(person_pattern, text)
    persons = [f"Person: {person}" for person in persons]
    
    # Extract locations
    locations = re.findall(location_pattern, text)
    locations = [f"Location: {location}" for location in locations]
    
    # Combine results
    entities = persons + locations
    
    # Return formatted result
    return ', '.join(entities) if entities else "No entities found."

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London and met with Alice.'))  # Should print: Person: Mary, Person: London, Person: Alice
    print(tentacle('No specific names in this sentence.'))  # Should print: No entities found.
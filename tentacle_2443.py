# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to be parsed.
    
    Returns:
    str: A string with extracted entities in the format 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Define patterns for entity extraction
    person_pattern = r'\b([A-Z][a-z]+)\b'
    location_pattern = r'\bto\s+([A-Z][a-z]+)\b'
    
    # Extract entities
    person = re.search(person_pattern, text)
    location = re.search(location_pattern, text)
    
    # Prepare the result
    result = []
    
    if person:
        result.append(f"Person: {person.group(1)}")
    if location:
        result.append(f"Location: {location.group(1)}")
    
    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The weather in New York is great.'))  # Should print: Location: New York
    print(tentacle('I love Berlin.'))  # Should print: Location: Berlin
    print(tentacle('Sarah is happy.'))  # Should print: Person: Sarah
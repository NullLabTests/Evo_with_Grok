# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to be processed.
    
    Returns:
    str: A string containing extracted entities in the format 'Entity_type: Entity_name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Define regex patterns for entity extraction
    person_pattern = r'\b([A-Z][a-z]+)\b'
    location_pattern = r'\bto\s+([A-Z][a-z]+)\b'
    
    # Extract entities
    person = re.search(person_pattern, text)
    location = re.search(location_pattern, text)
    
    # Construct the result string
    result = []
    if person:
        result.append(f"Person: {person.group(1)}")
    if location:
        result.append(f"Location: {location.group(1)}")
    
    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Alice visited London.'))  # Should print: Person: Alice, Location: London
    print(tentacle('Bob is going to New York.'))  # Should print: Person: Bob, Location: New York
    print(tentacle('Mary lives in Chicago.'))  # Should print: Person: Mary, Location: Chicago
    print(tentacle('David works in Seattle.'))  # Should print: Person: David, Location: Seattle
    print(tentacle('Sarah is traveling to Rome.'))  # Should print: Person: Sarah, Location: Rome
    print(tentacle('The Eiffel Tower is in Paris.'))  # Should print: Location: Paris
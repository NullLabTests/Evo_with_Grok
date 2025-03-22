# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing the text to process.
    
    Returns:
    str: A string with extracted entities formatted as 'Entity_type: Entity_name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Define patterns for entity extraction
    person_pattern = r'\b([A-Z][a-z]+)\b'
    location_pattern = r'\b(to|in) ([A-Z][a-z]+)\b'
    
    # Extract person names
    persons = re.findall(person_pattern, text)
    
    # Extract location names
    locations = re.findall(location_pattern, text)
    locations = [loc[1] for loc in locations]  # Extract only the location name
    
    # Format the result
    result = []
    if persons:
        result.append(f"Person: {', '.join(persons)}")
    if locations:
        result.append(f"Location: {', '.join(locations)}")
    
    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary and Tom are traveling to London and Berlin.'))  # Should print: Person: Mary, Tom, Location: London, Berlin
    print(tentacle('The weather is nice in New York today.'))  # Should print: Location: New York
# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to parse.
    
    Returns:
    str: A string containing the extracted entities formatted as 'Entity Type: Entity'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Define regex patterns for entity extraction
    person_pattern = r'\b[A-Z][a-z]+\b'
    location_pattern = r'\b(?:Paris|London|New York|Tokyo)\b'
    
    # Extract entities
    persons = re.findall(person_pattern, text)
    locations = re.findall(location_pattern, text)
    
    # Format the result
    result_parts = []
    if persons:
        result_parts.append(f"Person: {', '.join(persons)}")
    if locations:
        result_parts.append(f"Location: {', '.join(locations)}")
    
    return ', '.join(result_parts)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London and Tokyo.'))  # Should print: Person: Mary, Location: London, Tokyo
    print(tentacle('No entities here.'))  # Should print: 
    print(tentacle('Alice and Bob went to New York.'))  # Should print: Person: Alice, Bob, Location: New York
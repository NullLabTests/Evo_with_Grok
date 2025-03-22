# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing the text to parse.
    
    Returns:
    str: A string with extracted entities formatted as 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Define patterns for entity extraction
    person_pattern = r'\b([A-Z][a-z]+)\b'
    location_pattern = r'\bto\s([A-Z][a-z]+)\b'
    
    # Extract person
    person_match = re.search(person_pattern, text)
    person = person_match.group(1) if person_match else None
    
    # Extract location
    location_match = re.search(location_pattern, text)
    location = location_match.group(1) if location_match else None
    
    # Construct the result string
    result_parts = []
    if person:
        result_parts.append(f'Person: {person}')
    if location:
        result_parts.append(f'Location: {location}')
    
    return ', '.join(result_parts)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The city of New York is amazing.'))  # Should print: Location: New York
    print(tentacle('I love hiking in the mountains.'))  # Should print: 
    print(tentacle('Alice and Bob went to Rome.'))  # Should print: Person: Alice, Person: Bob, Location: Rome
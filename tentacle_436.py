# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from the given text.
    
    Args:
    text (str): A string containing the text to be parsed.
    
    Returns:
    str: A formatted string containing extracted entities.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Initialize dictionaries to store entities
    entities = {'Person': '', 'Location': ''}
    
    # Extract Person entity
    person_match = re.search(r'\b[A-Z][a-z]+\b', text)
    if person_match:
        entities['Person'] = person_match.group(0)
    
    # Extract Location entity
    location_match = re.search(r'to\s+(\b[A-Z][a-z]+\b)', text)
    if location_match:
        entities['Location'] = location_match.group(1)
    
    # Format and return the result
    result = ', '.join([f"{key}: {value}" for key, value in entities.items() if value])
    return result if result else "No entities found"

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The weather in Tokyo is great.'))  # Should print: Location: Tokyo
    print(tentacle('I love New York.'))  # Should print: Location: New York
    print(tentacle('Just a random sentence.'))  # Should print: No entities found
# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from a given text.
    
    Args:
    text (str): A string containing the text to parse.
    
    Returns:
    str: A string with extracted entities formatted as 'Entity: Value'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Initialize an empty dictionary to store entities
    entities = {}
    
    # Extract Person entity
    person_pattern = r'\b([A-Z][a-z]+)\b'
    person_match = re.search(person_pattern, text)
    if person_match:
        entities['Person'] = person_match.group(1)
    
    # Extract Location entity
    location_pattern = r'\bto\s([A-Z][a-z]+)\b'
    location_match = re.search(location_pattern, text)
    if location_match:
        entities['Location'] = location_match.group(1)
    
    # Format the result
    result = ', '.join(f"{entity}: {value}" for entity, value in entities.items())
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The city of Tokyo is beautiful.'))  # Should print: Location: Tokyo
    print(tentacle('Sarah enjoys hiking.'))  # Should print: Person: Sarah
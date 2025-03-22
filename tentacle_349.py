# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from a given text.
    
    Args:
    text (str): A string containing the text to parse.
    
    Returns:
    str: A formatted string with extracted entities.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Initialize dictionaries to store extracted entities
    entities = {
        'Person': None,
        'Location': None
    }
    
    # Extract Person entity (assuming it's the first word)
    person_match = re.match(r'^([A-Z][a-z]+)\b', text)
    if person_match:
        entities['Person'] = person_match.group(1)
    
    # Extract Location entity (assuming it's the last word)
    location_match = re.search(r'\b([A-Z][a-z]+)\.$', text)
    if location_match:
        entities['Location'] = location_match.group(1)
    
    # Format and return the result
    result = []
    for key, value in entities.items():
        if value:
            result.append(f"{key}: {value}")
    
    return ', '.join(result) if result else "No entities found."

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The cat sat on the mat.'))  # Should print: No entities found.
    print(tentacle('Alice and Bob went to Tokyo.'))  # Should print: Person: Alice, Location: Tokyo
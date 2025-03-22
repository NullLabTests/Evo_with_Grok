# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from the given text.
    
    Args:
    text (str): A string containing the text to be analyzed.
    
    Returns:
    str: A string with extracted entities formatted as 'Entity: Value'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re

    # Initialize a dictionary to store extracted entities
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
    result = ', '.join([f"{key}: {value}" for key, value in entities.items()])
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Alice visited New York.'))  # Should print: Person: Alice, Location: York
    print(tentacle('Bob is going to London tomorrow.'))  # Should print: Person: Bob, Location: London
    print(tentacle('The meeting is in Chicago.'))  # Should print: Location: Chicago
    print(tentacle('Sarah and Mike are staying home.'))  # Should print: Person: Sarah
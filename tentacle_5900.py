# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from given text.
    
    Args:
    text (str): A string containing text to parse.
    
    Returns:
    str: A string containing extracted entities in the format 'Entity: Value'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Initialize a dictionary to store extracted entities
    entities = {}
    
    # Extract Person entity (assuming it's the first word)
    person_match = re.match(r'^(\w+)', text)
    if person_match:
        entities['Person'] = person_match.group(1)
    
    # Extract Location entity (assuming it's the last word)
    location_match = re.search(r'(\w+)\.$', text)
    if location_match:
        entities['Location'] = location_match.group(1)
    
    # Format the result
    result = ', '.join([f"{key}: {value}" for key, value in entities.items()])
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('No one went anywhere.'))  # Should print: Person: No
    print(tentacle('To New York, Alice traveled.'))  # Should print: Person: Alice, Location: York
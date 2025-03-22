# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from the given text.
    
    Args:
    text (str): A string containing text to be analyzed.
    
    Returns:
    str: A string with extracted entities formatted as 'Entity: Value'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Initialize a dictionary to store extracted entities
    entities = {}
    
    # Extract Person (assuming it's the first word)
    person_match = re.match(r'^(\w+)', text)
    if person_match:
        entities['Person'] = person_match.group(1)
    
    # Extract Location (assuming it's the last word)
    location_match = re.search(r'(\w+)[.!]*$', text)
    if location_match:
        entities['Location'] = location_match.group(1)
    
    # Format the result string
    result = ', '.join([f"{key}: {value}" for key, value in entities.items()])
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited New York.'))  # Should print: Person: Mary, Location: York
    print(tentacle('No one went anywhere.'))  # Should print: Person: No
    print(tentacle('To London, Alice traveled.'))  # Should print: Person: To, Location: London
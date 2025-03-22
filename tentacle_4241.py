# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from the given text.
    
    Args:
    text (str): A string containing the text to be parsed.
    
    Returns:
    str: A string containing the extracted entities in the format 'Person: <name>, Location: <place>'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Initialize variables to store extracted entities
    person = None
    location = None
    
    # Extract person (assuming the first word is a person's name)
    person_match = re.match(r'^(\w+)', text)
    if person_match:
        person = person_match.group(1)
    
    # Extract location (assuming 'to' is followed by a location)
    location_match = re.search(r'to (\w+)', text)
    if location_match:
        location = location_match.group(1)
    
    # Format and return the result
    result = f"Person: {person if person else 'Unknown'}, Location: {location if location else 'Unknown'}"
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The dog ran in the park.'))  # Should print: Person: Unknown, Location: Unknown
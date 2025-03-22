# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from the given text.
    
    Args:
    text (str): A string containing the text to parse.
    
    Returns:
    str: A string with extracted entities formatted as 'Person: <name>, Location: <place>'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Initialize variables to store extracted entities
    person = None
    location = None
    
    # Extract person's name (assuming it's the first word in the sentence)
    person_match = re.match(r'^(\w+)', text)
    if person_match:
        person = person_match.group(1)
    
    # Extract location (assuming it's the last word in the sentence)
    location_match = re.search(r'(\w+)\.$', text)
    if location_match:
        location = location_match.group(1)
    
    # Format the result
    result = []
    if person:
        result.append(f"Person: {person}")
    if location:
        result.append(f"Location: {location}")
    
    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited New York.'))  # Should print: Person: Mary, Location: York
    print(tentacle('The cat sat on the mat.'))  # Should print: Person: The, Location: mat
    print(tentacle('In London, Alice met Bob.'))  # Should print: Person: In, Location: Bob
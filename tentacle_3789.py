# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from a given text.
    
    Args:
    text (str): A string containing text to be analyzed.
    
    Returns:
    str: A string containing extracted entities formatted as 'Entity: Value'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Initialize variables to store extracted entities
    person = None
    location = None
    
    # Extract person (assuming it's the first word in the sentence)
    person_match = re.match(r'^(\w+)', text)
    if person_match:
        person = person_match.group(1)
    
    # Extract location (assuming it's the last word in the sentence)
    location_match = re.search(r'(\w+)\.$', text)
    if location_match:
        location = location_match.group(1)
    
    # Construct the result string
    result = []
    if person:
        result.append(f"Person: {person}")
    if location:
        result.append(f"Location: {location}")
    
    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The cat sat on the mat.'))  # Should print: Person: The, Location: mat
    print(tentacle('I love New York.'))  # Should print: Person: I, Location: York
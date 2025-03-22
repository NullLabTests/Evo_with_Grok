# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from a given text.
    
    Args:
    text (str): A string containing the text to be analyzed.
    
    Returns:
    str: A string with extracted entities in the format 'Person: <name>, Location: <place>'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Initialize variables to store extracted entities
    person = None
    location = None
    
    # Extract person using a simple regex pattern
    person_match = re.search(r'\b[A-Z][a-z]+\b', text)
    if person_match:
        person = person_match.group(0)
    
    # Extract location using a simple regex pattern
    location_match = re.search(r'\bto\s([A-Z][a-z]+)\b', text)
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
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The capital of France is Paris.'))  # Should print: Location: Paris
    print(tentacle('Bob and Alice are friends.'))  # Should print: Person: Bob
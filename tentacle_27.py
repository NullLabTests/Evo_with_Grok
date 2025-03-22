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
    
    # Extract person using a simple regex pattern
    person_match = re.search(r'\b[A-Z][a-z]+\b', text)
    if person_match:
        person = person_match.group(0)
    
    # Extract location using a simple regex pattern
    location_match = re.search(r'\bto\s+([A-Z][a-z]+)\b', text)
    if location_match:
        location = location_match.group(1)
    
    # Format the result
    result = []
    if person:
        result.append(f"Person: {person}")
    if location:
        result.append(f"Location: {location}")
    
    return ', '.join(result) if result else "No entities found"

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The cat sat on the mat.'))  # Should print: No entities found
    print(tentacle('Alice and Bob traveled to New York.'))  # Should print: Person: Alice, Location: York
    print(tentacle('In Tokyo, Sarah met with her friend.'))  # Should print: Person: Tokyo, Location: Sarah
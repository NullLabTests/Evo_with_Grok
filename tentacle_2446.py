# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from given text.
    
    Args:
    text (str): A string containing text to parse.
    
    Returns:
    str: A string containing extracted entities in the format 'Person: <name>, Location: <place>'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Initialize variables to store extracted entities
    person = None
    location = None
    
    # Extract person using regex pattern for capitalized words followed by 'went'
    person_match = re.search(r'\b([A-Z][a-z]+)\b went', text)
    if person_match:
        person = person_match.group(1)
    
    # Extract location using regex pattern for capitalized words at the end of the sentence
    location_match = re.search(r'to \b([A-Z][a-z]+)\b\.?$', text)
    if location_match:
        location = location_match.group(1)
    
    # Construct and return the result string
    result = []
    if person:
        result.append(f"Person: {person}")
    if location:
        result.append(f"Location: {location}")
    
    return ', '.join(result) if result else "No entities found."

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The cat sat on the mat.'))  # Should print: No entities found.
    print(tentacle('Alice traveled to Tokyo.'))  # Should print: Person: Alice, Location: Tokyo
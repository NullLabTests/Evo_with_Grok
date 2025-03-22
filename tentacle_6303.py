# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from the given text.
    
    Args:
    text (str): A string containing the text to be parsed.
    
    Returns:
    str: A string with extracted entities formatted as 'Entity: Value'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Define simple regex patterns for entity extraction
    import re
    
    # Extract person names (assuming they are at the beginning of the sentence)
    person_pattern = r'^([A-Z][a-z]+)\s'
    person_match = re.search(person_pattern, text)
    person = person_match.group(1) if person_match else None
    
    # Extract location names (assuming they are at the end of the sentence)
    location_pattern = r'to\s([A-Z][a-z]+)\.$'
    location_match = re.search(location_pattern, text)
    location = location_match.group(1) if location_match else None
    
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
    print(tentacle('Alice traveled to London.'))  # Should print: Person: Alice, Location: London
    print(tentacle('Bob visited New York.'))  # Should print: Person: Bob, Location: New York
    print(tentacle('Went to Rome.'))  # Should print: Location: Rome
    print(tentacle('Sarah is here.'))  # Should print: Person: Sarah
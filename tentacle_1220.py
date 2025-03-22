# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from a given text.
    
    Args:
    text (str): A string containing the text to parse.
    
    Returns:
    str: A string with extracted entities in the format 'Person: <name>, Location: <place>'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Initialize variables to store extracted entities
    person = ''
    location = ''
    
    # Extract person name (assuming it's the first word)
    person_match = re.match(r'^([A-Z][a-z]+)\b', text)
    if person_match:
        person = person_match.group(1)
    
    # Extract location (assuming it's the last word)
    location_match = re.search(r'\b([A-Z][a-z]+)\.$', text)
    if location_match:
        location = location_match.group(1)
    
    # Format and return the result
    return f'Person: {person}, Location: {location}'

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('No one went anywhere.'))  # Should print: Person: , Location:
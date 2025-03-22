# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.
    
    This function uses regular expressions to identify and extract
    person names and location names from a given text.
    
    Args:
    text (str): A string containing the text to parse.
    
    Returns:
    str: A string containing the extracted entities in the format
         'Person: <name>, Location: <location>'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Initialize variables to store extracted entities
    person = ''
    location = ''
    
    # Extract person name (assuming it's the first word in the sentence)
    person_match = re.match(r'^(\w+)', text)
    if person_match:
        person = person_match.group(1)
    
    # Extract location (assuming it's the last word in the sentence)
    location_match = re.search(r'(\w+)\.$', text)
    if location_match:
        location = location_match.group(1)
    
    # Format and return the result
    result = f'Person: {person}, Location: {location}'
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('No one went anywhere.'))  # Should print: Person: No, Location: anywhere
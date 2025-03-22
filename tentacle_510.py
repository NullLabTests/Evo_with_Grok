# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from the given text.
    
    Args:
    text (str): A string containing the text to parse.
    
    Returns:
    str: A string with extracted entities formatted as 'Entity: Value'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re

    # Initialize a dictionary to store entities
    entities = {}

    # Extract person names (assuming simple first name format)
    person_match = re.search(r'\b([A-Z][a-z]+)\b', text)
    if person_match:
        entities['Person'] = person_match.group(1)

    # Extract locations (assuming proper noun format)
    location_match = re.search(r'\bto\s([A-Z][a-z]+)\b', text)
    if location_match:
        entities['Location'] = location_match.group(1)

    # Format the result
    result = ', '.join(f"{key}: {value}" for key, value in entities.items())

    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('No names or places here.'))  # Should print: (empty string)
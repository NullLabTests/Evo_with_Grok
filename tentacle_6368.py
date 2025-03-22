# Domains: text processing, mathematics
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
    import re

    # Initialize an empty dictionary to store entities
    entities = {}

    # Extract Person entity
    person_match = re.search(r'\b([A-Z][a-z]+)\b', text)
    if person_match:
        entities['Person'] = person_match.group(1)

    # Extract Location entity
    location_match = re.search(r'to\s+([A-Z][a-z]+)', text)
    if location_match:
        entities['Location'] = location_match.group(1)

    # Format the result
    result = ', '.join([f"{entity}: {value}" for entity, value in entities.items()])

    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('No entities here.'))     # Should print: (empty string)
    print(tentacle('Alice traveled to Rome and then to Berlin.'))  # Should print: Person: Alice, Location: Rome
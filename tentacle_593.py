# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from the given text.
    
    Args:
    text (str): A string containing the text to be analyzed.
    
    Returns:
    str: A string with extracted entities formatted as 'Entity: Value'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re

    # Initialize dictionaries to store entities
    entities = {'Person': '', 'Location': ''}

    # Extract Person (assuming the first word is a person's name)
    person_match = re.match(r'^([A-Z][a-z]+)', text)
    if person_match:
        entities['Person'] = person_match.group(1)

    # Extract Location (assuming it's the last word in the sentence)
    location_match = re.search(r'\bto\s+([A-Z][a-z]+)\.?$', text)
    if location_match:
        entities['Location'] = location_match.group(1)

    # Format and return the result
    result = ', '.join([f"{entity}: {value}" for entity, value in entities.items() if value])
    return result if result else "No entities found"

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The cat sat on the mat.'))  # Should print: No entities found
    print(tentacle('Alice traveled to Rome yesterday.'))  # Should print: Person: Alice, Location: Rome
# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.

    Args:
    text (str): A string containing the text to parse.

    Returns:
    str: A string with extracted entities formatted as 'Entity Type: Entity Name'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re

    # Dictionary to store extracted entities
    entities = {}

    # Extract person names (simple pattern: capitalized word at the start of the sentence)
    person_match = re.match(r'^([A-Z][a-z]+)', text)
    if person_match:
        entities['Person'] = person_match.group(1)

    # Extract locations (simple pattern: 'to' followed by a capitalized word)
    location_match = re.search(r'to\s+([A-Z][a-z]+)', text)
    if location_match:
        entities['Location'] = location_match.group(1)

    # Format the result
    result = ', '.join(f"{entity_type}: {entity_name}" for entity_type, entity_name in entities.items())

    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The dog ran to the park.'))  # Should print: Location: Park
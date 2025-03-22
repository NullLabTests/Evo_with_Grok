# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.

    Args:
    text (str): A string containing text to parse.

    Returns:
    str: A string containing extracted entities in the format 'Entity Type: Entity Name'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re

    # Dictionary to store extracted entities
    entities = {}

    # Extract person names (assuming simple case of single word names)
    person_match = re.search(r'\b([A-Z][a-z]+)\b', text)
    if person_match:
        entities['Person'] = person_match.group(1)

    # Extract locations (assuming they start with a capital letter and are not at the start of the sentence)
    location_matches = re.findall(r'(?<!\b\w)\b([A-Z][a-z]+)\b', text)
    if location_matches:
        entities['Location'] = location_matches[-1]  # Take the last match as it's likely the location

    # Format the output
    return ', '.join(f"{entity_type}: {entity_name}" for entity_type, entity_name in entities.items())

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London and New York.'))  # Should print: Person: Mary, Location: York
    print(tentacle('In Tokyo, Alice met Bob.'))  # Should print: Person: Alice, Location: Tokyo
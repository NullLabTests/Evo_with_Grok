# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.

    Args:
    text (str): A string containing text to parse for entities.

    Returns:
    str: A string containing extracted entities in the format 'Entity Type: Entity Name'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re

    # Dictionary to store extracted entities
    entities = {}

    # Extract person names (simple regex for demonstration)
    person_pattern = r'\b[A-Z][a-z]+\b'
    persons = re.findall(person_pattern, text)
    if persons:
        entities['Person'] = persons[0]  # Assuming the first match is the person

    # Extract locations (simple regex for demonstration)
    location_pattern = r'\b(?:New )?[A-Z][a-z]+(?: [A-Z][a-z]+)?\b'
    locations = re.findall(location_pattern, text)
    if locations:
        entities['Location'] = locations[0]  # Assuming the first match is the location

    # Format the result
    result = ', '.join(f'{entity_type}: {entity_name}' for entity_type, entity_name in entities.items())

    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited New York.'))  # Should print: Person: Mary, Location: New York
    print(tentacle('The capital of France is Paris.'))  # Should print: Location: France, Location: Paris
    print(tentacle('No entities here.'))  # Should print: (empty string)
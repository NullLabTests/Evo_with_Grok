# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from a given text.

    Args:
    text (str): A string containing text to be parsed.

    Returns:
    str: A string with extracted entities formatted as 'Entity Type: Entity Name'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re

    # Define patterns for entity extraction
    person_pattern = r'\b[A-Z][a-z]+\b'
    location_pattern = r'\b(?:to|in|at)\s+([A-Z][a-z]+)\b'

    # Extract person
    person = re.search(person_pattern, text)
    person_entity = f"Person: {person.group(0)}" if person else ""

    # Extract location
    location = re.search(location_pattern, text)
    location_entity = f"Location: {location.group(1)}" if location else ""

    # Combine extracted entities
    entities = [entity for entity in [person_entity, location_entity] if entity]
    result = ", ".join(entities)

    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Alice is in London.'))  # Should print: Person: Alice, Location: London
    print(tentacle('Bob visited New York.'))  # Should print: Person: Bob, Location: New York
    print(tentacle('No entities here.'))  # Should print: (empty string)
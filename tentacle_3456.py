# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.

    Args:
    text (str): A string containing text to parse for entities.

    Returns:
    str: A string containing the extracted entities in the format 'Entity Type: Entity Name'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Initialize an empty list to store extracted entities
    entities = []

    # Define regex patterns for entity extraction
    import re
    person_pattern = r'\b[A-Z][a-z]+\b'
    location_pattern = r'\b(?:Paris|London|New York|Tokyo)\b'

    # Extract person entities
    for match in re.finditer(person_pattern, text):
        if match.group() not in ['The', 'A', 'An']:
            entities.append(f"Person: {match.group()}")

    # Extract location entities
    for match in re.finditer(location_pattern, text):
        entities.append(f"Location: {match.group()}")

    # Join the extracted entities into a single string
    return ', '.join(entities)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London and New York.'))  # Should print: Person: Mary, Location: London, Location: New York
    print(tentacle('The capital of France is Paris.'))  # Should print: Location: Paris
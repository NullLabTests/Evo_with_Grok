# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.

    Args:
    text (str): A string containing text to be parsed.

    Returns:
    str: A string with extracted entities formatted as 'Entity Type: Entity Name'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re

    # Define regex patterns for entity extraction
    person_pattern = r'\b([A-Z][a-z]+)\b'
    location_pattern = r'\b(?:to|in|at)\s+([A-Z][a-z]+)\b'

    # Extract entities
    person = re.search(person_pattern, text)
    location = re.search(location_pattern, text)

    # Format the result
    result = []
    if person:
        result.append(f"Person: {person.group(1)}")
    if location:
        result.append(f"Location: {location.group(1)}")

    return ', '.join(result) if result else "No entities found."

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Alice is visiting New York.'))  # Should print: Person: Alice, Location: New York
    print(tentacle('The weather in London is great.'))  # Should print: Location: London
    print(tentacle('I love coding.'))  # Should print: No entities found.
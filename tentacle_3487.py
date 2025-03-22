# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.

    Args:
    text (str): A string containing text to parse for entities.

    Returns:
    str: A formatted string containing extracted entities.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re

    # Define regex patterns for entity extraction
    person_pattern = r'\b([A-Z][a-z]+)\b'
    location_pattern = r'\b(?:to|in|at)\s+([A-Z][a-z]+)\b'

    # Extract person
    person = re.search(person_pattern, text)
    person_name = person.group(1) if person else None

    # Extract location
    location = re.search(location_pattern, text)
    location_name = location.group(1) if location else None

    # Format and return the result
    result_parts = []
    if person_name:
        result_parts.append(f"Person: {person_name}")
    if location_name:
        result_parts.append(f"Location: {location_name}")

    return ', '.join(result_parts) if result_parts else "No entities found"

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary is visiting London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The weather in Tokyo is great.'))  # Should print: Location: Tokyo
    print(tentacle('I love programming.'))  # Should print: No entities found
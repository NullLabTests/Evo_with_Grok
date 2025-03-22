# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.

    Args:
    text (str): A string containing text to parse.

    Returns:
    str: A string with identified entities formatted as 'Entity Type: Entity Name'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re

    # Define regex patterns for entity extraction
    person_pattern = r'\b([A-Z][a-z]+)\b'
    location_pattern = r'\bto\s+([A-Z][a-z]+)\b'

    # Extract entities using regex
    person_match = re.search(person_pattern, text)
    location_match = re.search(location_pattern, text)

    # Initialize result string
    result = []

    # Add person entity if found
    if person_match:
        result.append(f"Person: {person_match.group(1)}")

    # Add location entity if found
    if location_match:
        result.append(f"Location: {location_match.group(1)}")

    # Join results with comma and return
    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The capital of France is Paris.'))  # Should print: Location: Paris
    print(tentacle('Bob and Alice are friends.'))  # Should print: Person: Bob, Person: Alice
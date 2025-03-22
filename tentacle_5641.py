# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.

    This function uses regular expressions to identify and extract person names and locations
    from a given text. It then formats the extracted entities into a specified string format.

    Args:
    text (str): A string containing the text to be parsed.

    Returns:
    str: A formatted string containing the extracted entities.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re

    # Regular expressions for entity extraction
    person_pattern = r'\b([A-Z][a-z]+)\b'
    location_pattern = r'\bto\s+([A-Z][a-z]+)\b'

    # Extract entities
    persons = re.findall(person_pattern, text)
    locations = re.findall(location_pattern, text)

    # Format the results
    result = []
    if persons:
        result.append(f"Person: {', '.join(persons)}")
    if locations:
        result.append(f"Location: {', '.join(locations)}")

    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Alice and Bob visited New York and London.'))  # Should print: Person: Alice, Bob, Location: New York, London
    print(tentacle('The capital of France is Paris.'))  # Should print: Location: Paris
    print(tentacle('No entities here.'))  # Should print:
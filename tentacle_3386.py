# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.

    This function uses regular expressions to identify and extract
    person names and locations from a given text. It then formats
    the extracted entities into a string.

    Args:
    text (str): A string containing text to be processed.

    Returns:
    str: A formatted string of extracted entities.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re

    # Regular expressions for entity extraction
    person_pattern = r'\b([A-Z][a-z]+)\b'
    location_pattern = r'\bto\s+([A-Z][a-z]+)\b'

    # Extract person name
    person_match = re.search(person_pattern, text)
    person = person_match.group(1) if person_match else None

    # Extract location
    location_match = re.search(location_pattern, text)
    location = location_match.group(1) if location_match else None

    # Format the result
    result_parts = []
    if person:
        result_parts.append(f"Person: {person}")
    if location:
        result_parts.append(f"Location: {location}")

    return ', '.join(result_parts) if result_parts else "No entities found."

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The weather is nice today.'))  # Should print: No entities found.
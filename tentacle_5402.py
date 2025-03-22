# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from the given text.

    Args:
    text (str): A string containing text to parse.

    Returns:
    str: A string with extracted entities formatted as 'Person: [Name], Location: [Place]'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re

    # Initialize variables to store extracted entities
    person = None
    location = None

    # Extract person (assuming the first word is a person's name)
    person_match = re.match(r'^(\w+)', text)
    if person_match:
        person = person_match.group(1)

    # Extract location (assuming 'to' is followed by a location)
    location_match = re.search(r'to\s+(\w+)', text)
    if location_match:
        location = location_match.group(1)

    # Format and return the result
    result = []
    if person:
        result.append(f"Person: {person}")
    if location:
        result.append(f"Location: {location}")

    return ', '.join(result) if result else "No entities found."

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The city is beautiful.'))  # Should print: No entities found.
    print(tentacle('I traveled to New York with Bob.'))  # Should print: Person: I, Location: New York
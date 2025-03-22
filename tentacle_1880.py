# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from a given text.

    Args:
    text (str): A string containing text to parse.

    Returns:
    str: A string with extracted entities formatted as 'Person: <name>, Location: <place>'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re

    # Initialize variables to store extracted entities
    person = None
    location = None

    # Extract person's name (assuming it's the first word in the sentence)
    person_match = re.match(r'^([A-Z][a-z]+)', text)
    if person_match:
        person = person_match.group(1)

    # Extract location (assuming it's the last word in the sentence)
    location_match = re.search(r'([A-Z][a-z]+)\.$', text)
    if location_match:
        location = location_match.group(1)

    # Format the result string
    result = []
    if person:
        result.append(f"Person: {person}")
    if location:
        result.append(f"Location: {location}")

    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The Eiffel Tower is in Paris.'))  # Should print: Location: Paris
    print(tentacle('Hello world.'))  # Should print: (empty string)
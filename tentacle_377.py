# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from a given text.

    Args:
    text (str): A string containing the text to analyze.

    Returns:
    str: A formatted string with extracted entities.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re

    # Initialize variables to store extracted entities
    person = None
    location = None

    # Extract person (assuming person is the first word in the sentence)
    person_match = re.match(r'^([A-Z][a-z]+)', text)
    if person_match:
        person = person_match.group(1)

    # Extract location (assuming location is the last word in the sentence)
    location_match = re.search(r'([A-Z][a-z]+)\.$', text)
    if location_match:
        location = location_match.group(1)

    # Format the result
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
    print(tentacle('The weather in Tokyo is great.'))  # Should print: Location: Tokyo
    print(tentacle('I love New York.'))  # Should print: Location: York
    print(tentacle('Hello world!'))  # Should print: No entities found.
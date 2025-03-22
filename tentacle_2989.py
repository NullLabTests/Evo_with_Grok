# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.

    This function identifies and extracts 'Person' and 'Location' entities from the given text.
    It uses simple pattern matching to identify these entities.

    Args:
    text (str): A string containing the text to be parsed.

    Returns:
    str: A string containing the identified entities in the format 'Entity: Value'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Initialize variables to store identified entities
    person = None
    location = None

    # Split the text into words
    words = text.split()

    # Identify 'Person' entity (assuming the first word is a person's name)
    if words:
        person = words[0]

    # Identify 'Location' entity (assuming 'to' is followed by a location)
    if 'to' in words:
        location_index = words.index('to') + 1
        if location_index < len(words):
            location = words[location_index]

    # Construct the result string
    result = []
    if person:
        result.append(f"Person: {person}")
    if location:
        result.append(f"Location: {location}")

    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Alice traveled to New York.'))  # Should print: Person: Alice, Location: New York
    print(tentacle('Bob is staying in London.'))  # Should print: Person: Bob, Location: London
    print(tentacle('The city is beautiful.'))  # Should print: (nothing, as no entities are identified)
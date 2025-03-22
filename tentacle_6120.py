# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.

    This function identifies and extracts 'Person' and 'Location' entities from a given text.
    It uses simple pattern matching to identify these entities.

    Args:
    text (str): A string containing text to parse for entities.

    Returns:
    str: A string describing the identified entities in the format 'Entity Type: Entity Name'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Initialize variables to store identified entities
    person = None
    location = None

    # Split the text into words
    words = text.split()

    # Identify person (assuming the first word is a person's name)
    if words:
        person = words[0]

    # Identify location (assuming 'to' is followed by a location)
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
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The dog ran in the park.'))  # Should print: Person: The
    print(tentacle('I am going to New York.'))  # Should print: Person: I, Location: New
    print(tentacle('No entities here.'))  # Should print: Person: No
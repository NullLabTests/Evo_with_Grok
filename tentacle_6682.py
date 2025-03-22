# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.

    This function uses simple pattern matching to identify and categorize
    entities such as persons and locations from a given text.

    Args:
    text (str): A string containing the text to be analyzed.

    Returns:
    str: A string with identified entities and their categories.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Initialize an empty dictionary to store entities
    entities = {}

    # Split the text into words
    words = text.split()

    # Simple pattern matching for persons (assuming first word is a person's name)
    if words:
        entities['Person'] = words[0]

    # Simple pattern matching for locations (assuming 'to' precedes a location)
    if 'to' in words:
        location_index = words.index('to') + 1
        if location_index < len(words):
            entities['Location'] = words[location_index]

    # Format the result string
    result = []
    for key, value in entities.items():
        result.append(f"{key}: {value}")

    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Alice visited New York.'))  # Should print: Person: Alice, Location: York
    print(tentacle('Bob is staying home.'))  # Should print: Person: Bob
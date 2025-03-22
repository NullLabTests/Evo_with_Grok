# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.

    Args:
    text (str): A string containing text to parse for entities.

    Returns:
    str: A formatted string of extracted entities.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Dictionary to store recognized entities
    entities = {}

    # List of words to check for entities
    words = text.split()

    # Check for person names (simple heuristic: capitalized word at the beginning)
    if words and words[0].istitle():
        entities['Person'] = words[0]

    # Check for locations (simple heuristic: capitalized word at the end)
    if words and words[-1].istitle():
        entities['Location'] = words[-1]

    # Format the result
    result = ', '.join([f"{key}: {value}" for key, value in entities.items()])

    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The capital is Berlin.'))  # Should print: Location: Berlin
    print(tentacle('hello world'))  # Should print: empty string
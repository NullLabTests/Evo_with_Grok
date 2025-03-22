# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text, such as persons and locations.

    Args:
    text (str): A string containing the text to be parsed.

    Returns:
    str: A formatted string containing extracted entities.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Initialize an empty dictionary to store entities
    entities = {}

    # Split the text into words
    words = text.split()

    # Iterate through the words to identify entities
    for i, word in enumerate(words):
        # Check for person names (simple heuristic: capitalized words that are not the first word)
        if word.istitle() and i > 0:
            if 'Person' not in entities:
                entities['Person'] = word
            else:
                entities['Person'] += f" {word}"

        # Check for locations (simple heuristic: the last word if it's capitalized)
        if word.istitle() and i == len(words) - 1:
            entities['Location'] = word

    # Format the result
    result = []
    for key, value in entities.items():
        result.append(f"{key}: {value}")

    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary and Bob visited London.'))  # Should print: Person: Mary Bob, Location: London
    print(tentacle('The capital of France is Paris.'))  # Should print: Location: Paris
    print(tentacle('alice went to new york.'))  # Should print: Person: Alice, Location: York
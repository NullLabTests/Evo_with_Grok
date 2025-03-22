# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text, specifically identifying persons and locations.

    Args:
    text (str): A string containing the text to be parsed.

    Returns:
    str: A formatted string containing identified entities.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Initialize an empty dictionary to store identified entities
    entities = {}

    # Split the text into words
    words = text.split()

    # Iterate through the words to identify entities
    for i, word in enumerate(words):
        # Check for person names (simple heuristic: capitalized words not at the start of the sentence)
        if word.istitle() and i > 0:
            if 'Person' not in entities:
                entities['Person'] = word
            else:
                entities['Person'] += f" {word}"

        # Check for location names (simple heuristic: 'to' followed by a capitalized word)
        if i > 0 and words[i-1].lower() == 'to' and word.istitle():
            if 'Location' not in entities:
                entities['Location'] = word
            else:
                entities['Location'] += f" {word}"

    # Format the result string
    result = []
    for key, value in entities.items():
        result.append(f"{key}: {value}")

    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary and Tom visited New York.'))  # Should print: Person: Mary Tom, Location: New York
    print(tentacle('The capital of France is Paris.'))  # Should print: Location: France Paris
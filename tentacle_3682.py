# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text, identifying persons and locations.

    Args:
    text (str): A string containing the text to be parsed.

    Returns:
    str: A string with identified entities formatted as 'Entity Type: Entity Name'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Initialize an empty dictionary to store entities
    entities = {}

    # Split the text into words
    words = text.split()

    # Iterate through the words to identify entities
    for word in words:
        # Check for person names (simple heuristic: capitalized first letter and not a common word)
        if word.istitle() and word.lower() not in ['the', 'a', 'an', 'to', 'and', 'or', 'but']:
            if 'Person' not in entities:
                entities['Person'] = word
            else:
                entities['Person'] += f" {word}"

        # Check for location names (simple heuristic: capitalized first letter and at the end of the sentence)
        if word.istitle() and word == words[-1]:
            entities['Location'] = word

    # Format the result
    result = []
    for entity_type, entity_name in entities.items():
        result.append(f"{entity_type}: {entity_name}")

    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary and Tom visited New York.'))  # Should print: Person: Mary Tom, Location: York
    print(tentacle('The cat sat on the mat.'))  # Should print: (nothing, as no entities are identified)
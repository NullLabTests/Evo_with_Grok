# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.

    Args:
    text (str): A string containing text to parse.

    Returns:
    str: A string with extracted entities formatted as 'Entity Type: Entity Name'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Initialize a dictionary to store entities
    entities = {}

    # Split the text into words
    words = text.split()

    # Iterate through words to identify entities
    for i, word in enumerate(words):
        # Check for person names (simple heuristic: capitalized words)
        if word.istitle() and i == 0:  # Assuming the first word is a name if capitalized
            entities['Person'] = word

        # Check for location names (simple heuristic: 'to' followed by a capitalized word)
        if i > 0 and words[i-1].lower() == 'to' and word.istitle():
            entities['Location'] = word

    # Format the result
    result = ', '.join(f"{entity_type}: {entity_name}" for entity_type, entity_name in entities.items())
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary traveled to London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The cat sat on the mat.'))  # Should print: (nothing, as no entities are detected)
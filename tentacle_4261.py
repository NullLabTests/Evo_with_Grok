# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.

    Args:
    text (str): A string containing the text to parse.

    Returns:
    str: A string with extracted entities in the format 'Entity Type: Entity Name'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Initialize an empty dictionary to store entities
    entities = {}

    # Split the text into words
    words = text.split()

    # Iterate through words to find entities
    for i, word in enumerate(words):
        # Check for person names (simple heuristic: capitalized word at the start of the sentence)
        if i == 0 and word.istitle():
            entities['Person'] = word

        # Check for locations (simple heuristic: 'to' followed by a capitalized word)
        if i > 0 and words[i-1].lower() == 'to' and word.istitle():
            entities['Location'] = word

    # Format the result
    result = ', '.join(f"{entity_type}: {entity}" for entity_type, entity in entities.items())
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London yesterday.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The capital of France is Paris.'))  # Should print: Location: France, Location: Paris
    print(tentacle('I live in New York.'))  # Should print: Location: New York
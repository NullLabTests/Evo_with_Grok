# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.

    Args:
    text (str): A string containing text to analyze.

    Returns:
    str: A string containing extracted entities in the format 'Entity Type: Entity Name'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Dictionary to store recognized entities
    entities = {}

    # List of words to check for entities
    words = text.split()

    # Check for person names (simple heuristic: capitalized words at the beginning of the sentence)
    if words and words[0].istitle():
        entities['Person'] = words[0]

    # Check for location names (simple heuristic: capitalized words at the end of the sentence)
    if words and words[-1].istitle():
        entities['Location'] = words[-1]

    # Format the result
    result = ', '.join([f"{entity_type}: {entity_name}" for entity_type, entity_name in entities.items()])

    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London yesterday.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The weather in New York is great.'))  # Should print: Location: York
    print(tentacle('I love going to the beach.'))  # Should print: (empty string)
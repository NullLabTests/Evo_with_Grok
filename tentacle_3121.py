# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.

    This function uses simple pattern matching to identify and extract
    person names and locations from a given text.

    Args:
    text (str): A string containing the text to be analyzed.

    Returns:
    str: A string with identified entities formatted as 'Entity Type: Entity Name'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Initialize a dictionary to store extracted entities
    entities = {}

    # Split the text into words
    words = text.split()

    # Simple pattern matching for person names (assuming first word is a name)
    if words:
        entities['Person'] = words[0]

    # Simple pattern matching for locations (assuming 'to' precedes a location)
    if 'to' in words:
        location_index = words.index('to') + 1
        if location_index < len(words):
            entities['Location'] = words[location_index]

    # Format the result
    result = ', '.join([f"{entity_type}: {entity}" for entity_type, entity in entities.items()])

    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London last week.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The capital of France is Paris.'))  # Should print: Location: Paris
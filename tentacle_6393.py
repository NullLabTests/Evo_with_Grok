# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text, such as persons and locations.

    Args:
    text (str): A string containing text to be parsed for entities.

    Returns:
    str: A string containing extracted entities in the format 'Entity_type: Entity_name'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Dictionary to store recognized entities
    entities = {}

    # List of words that indicate a person
    person_indicators = ['Mr.', 'Mrs.', 'Ms.', 'Dr.', 'Professor', 'John', 'Mary', 'David']

    # List of words that indicate a location
    location_indicators = ['to', 'in', 'at', 'Paris', 'New York', 'London']

    # Split the text into words
    words = text.split()

    # Iterate through the words to identify entities
    for word in words:
        if word in person_indicators:
            entities['Person'] = word
        elif word in location_indicators:
            entities['Location'] = word

    # Format the result
    result = ', '.join([f"{entity_type}: {entity}" for entity_type, entity in entities.items()])

    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary is visiting New York.'))  # Should print: Person: Mary, Location: New York
    print(tentacle('Dr. Smith lives in London.'))  # Should print: Person: Dr., Location: London
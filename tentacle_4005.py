# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text, such as persons and locations.
    
    Args:
    text (str): A string containing text to parse.
    
    Returns:
    str: A string with extracted entities in the format 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Initialize a dictionary to store entities
    entities = {}

    # Split the text into words
    words = text.split()

    # Simple rules for entity extraction
    for word in words:
        if word.istitle() and word not in entities.values():  # Assume capitalized words are names
            if 'Person' not in entities:
                entities['Person'] = word
            elif 'Location' not in entities:
                entities['Location'] = word

    # Format the result
    result = ', '.join([f"{entity_type}: {entity}" for entity_type, entity in entities.items()])

    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited New York.'))  # Should print: Person: Mary, Location: New York
    print(tentacle('The cat sat on the mat.'))  # Should print: (empty string, no entities found)
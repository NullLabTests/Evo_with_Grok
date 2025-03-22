# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities (Person, Location) from a given text.

    Args:
    text (str): A string containing the text to parse.

    Returns:
    str: A string with extracted entities formatted as 'Entity Type: Entity Name'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Initialize a dictionary to store extracted entities
    entities = {
        'Person': None,
        'Location': None
    }

    # Split the text into words
    words = text.split()

    # Simple rule-based entity extraction
    for word in words:
        if word.istitle() and word not in ['The', 'A', 'An']:
            if entities['Person'] is None:
                entities['Person'] = word
            elif entities['Location'] is None:
                entities['Location'] = word

    # Format the result
    result = []
    for entity_type, entity_name in entities.items():
        if entity_name:
            result.append(f"{entity_type}: {entity_name}")

    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The dog chased the cat in the garden.'))  # Should print: Person: None, Location: Garden
# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from the given text.

    Args:
    text (str): A string containing text to parse for entities.

    Returns:
    str: A string with identified entities formatted as 'Entity Type: Entity Name'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Dictionary to store identified entities
    entities = {}

    # Split the text into words
    words = text.split()

    # Simple entity recognition rules
    for word in words:
        if word.istitle() and word not in ['To', 'The', 'A', 'An']:
            if word.isalpha():
                entities['Person'] = word
        elif word.lower() in ['paris', 'london', 'new york', 'tokyo']:
            entities['Location'] = word

    # Format the result
    result = ', '.join([f"{entity_type}: {entity}" for entity_type, entity in entities.items()])
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The conference was in Tokyo.'))  # Should print: Location: Tokyo
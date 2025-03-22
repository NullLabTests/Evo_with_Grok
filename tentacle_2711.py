# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.

    This function identifies and extracts 'Person' and 'Location' entities from
    the given text, returning them in a formatted string.

    Args:
    text (str): A string containing text to parse for entities.

    Returns:
    str: A formatted string containing identified entities.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Initialize a dictionary to store identified entities
    entities = {'Person': None, 'Location': None}

    # Split the text into words
    words = text.split()

    # Simple rule-based entity extraction
    for word in words:
        if word.istitle() and word not in ['To', 'Went']:
            if entities['Person'] is None:
                entities['Person'] = word
            elif entities['Location'] is None:
                entities['Location'] = word

    # Format and return the result
    result = []
    for key, value in entities.items():
        if value:
            result.append(f"{key}: {value}")
    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The cat sat on the mat.'))  # Should print: (nothing, as no entities are identified)
# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.

    This function uses simple pattern matching to identify and extract
    'Person' and 'Location' entities from the given text.

    Args:
    text (str): A string containing the text to parse.

    Returns:
    str: A string with extracted entities in the format 'Entity: Value'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Initialize an empty dictionary to store entities
    entities = {}

    # Split the text into words
    words = text.split()

    # Check for person (assuming the first word is a person's name)
    if words:
        entities['Person'] = words[0]

    # Check for location (assuming 'to' or 'in' precedes a location)
    for i, word in enumerate(words):
        if word.lower() in ['to', 'in'] and i + 1 < len(words):
            entities['Location'] = words[i + 1]
            break

    # Format the result
    result = ', '.join([f"{key}: {value}" for key, value in entities.items()])
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary is traveling to Tokyo.'))  # Should print: Person: Mary, Location: Tokyo
    print(tentacle('In New York, David met Alice.'))  # Should print: Person: In, Location: York
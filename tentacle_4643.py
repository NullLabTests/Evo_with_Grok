# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from a given text.

    Args:
    text (str): A string containing text to be parsed for entities.

    Returns:
    str: A string with extracted entities formatted as 'Person: <name>, Location: <place>'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Initialize dictionaries to store entities
    entities = {'Person': '', 'Location': ''}

    # Split the text into words
    words = text.split()

    # Simple rule-based entity extraction
    for word in words:
        if word[0].isupper() and word.lower() not in ['to', 'went']:
            if not entities['Person']:
                entities['Person'] = word
            elif not entities['Location']:
                entities['Location'] = word

    # Format the result
    result = ', '.join([f"{key}: {value}" for key, value in entities.items() if value])
    return result if result else "No entities found."

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The cat sat on the mat.'))  # Should print: No entities found.
    print(tentacle('Alice and Bob went to New York.'))  # Should print: Person: Alice, Location: New York
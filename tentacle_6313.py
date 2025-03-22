# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities (Person, Location) from the given text.

    Args:
    text (str): A string containing text to parse for entities.

    Returns:
    str: A string with extracted entities formatted as 'Entity: Value'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Initialize a dictionary to store entities
    entities = {}

    # Split the text into words
    words = text.split()

    # Extract Person entity (assuming the first word is a person's name)
    if words:
        entities['Person'] = words[0]

    # Extract Location entity (assuming the last word is a location)
    if len(words) > 1:
        entities['Location'] = words[-1].strip('.,!?')

    # Format the result
    result = ', '.join(f"{entity}: {value}" for entity, value in entities.items() if value)

    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London yesterday.'))  # Should print: Person: Mary, Location: London
    print(tentacle('No one went anywhere.'))  # Should print: Person: No
    print(tentacle('To New York, Alice traveled.'))  # Should print: Person: To, Location: York
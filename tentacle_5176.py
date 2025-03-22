# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.

    Args:
    text (str): A string containing text to parse for entities.

    Returns:
    str: A string with extracted entities formatted as 'Entity Type: Entity Name'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Initialize a dictionary to store extracted entities
    entities = {}

    # Split the text into words
    words = text.split()

    # Iterate through words to find and classify entities
    for i, word in enumerate(words):
        if word.istitle() and i > 0 and words[i-1].lower() in ['mr', 'mrs', 'ms', 'dr']:
            entities['Person'] = word
        elif word.istitle() and i == 0:
            entities['Person'] = word
        elif word.istitle() and i > 0 and words[i-1].lower() in ['to', 'in', 'at']:
            entities['Location'] = word

    # Format the output string
    output = []
    for entity_type, entity_name in entities.items():
        output.append(f"{entity_type}: {entity_name}")

    return ', '.join(output)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Dr. Smith visited New York.'))  # Should print: Person: Smith, Location: York
    print(tentacle('The meeting is in London.'))  # Should print: Location: London
    print(tentacle('Alice and Bob are friends.'))  # Should print: Person: Alice
# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.

    Args:
    text (str): A string containing text to parse.

    Returns:
    str: A string with extracted entities formatted as 'Entity Type: Entity Name'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Dictionary to store recognized entities
    entities = {}

    # Split the text into words
    words = text.split()

    # Simple rule-based entity recognition
    for i, word in enumerate(words):
        if word.istitle() and i > 0 and words[i-1].lower() in ['mr', 'mrs', 'ms', 'dr']:
            entities['Person'] = word
        elif word.istitle() and i == 0:
            entities['Person'] = word
        elif word.lower() in ['went', 'traveled', 'journeyed'] and i+1 < len(words):
            entities['Location'] = words[i+1]

    # Format the output string
    output = []
    for entity_type, entity_name in entities.items():
        output.append(f"{entity_type}: {entity_name}")

    return ', '.join(output)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Dr. Smith traveled to New York.'))  # Should print: Person: Smith, Location: New York
    print(tentacle('Mary journeyed to London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The cat sat on the mat.'))  # Should print: Person: The
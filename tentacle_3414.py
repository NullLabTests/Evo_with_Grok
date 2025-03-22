# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.

    Args:
    text (str): A string containing text to parse for entities.

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

    # Iterate through words to identify entities
    for i, word in enumerate(words):
        # Check for person names (assuming capitalized words at the start of a sentence)
        if word.istitle() and (i == 0 or words[i-1] in ['.', '!', '?']):
            entities['Person'] = word
        
        # Check for locations (assuming capitalized words after 'to', 'in', 'at')
        if word.lower() in ['to', 'in', 'at'] and i+1 < len(words) and words[i+1].istitle():
            entities['Location'] = words[i+1]

    # Format the result
    result = ', '.join([f"{entity_type}: {entity}" for entity_type, entity in entities.items()])
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary is visiting London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The meeting is in Tokyo.'))  # Should print: Location: Tokyo
    print(tentacle('hello world'))  # Should print: (empty string)
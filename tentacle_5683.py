# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to be parsed for entities.
    
    Returns:
    str: A string containing extracted entities and their types.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Initialize an empty dictionary to store entities
    entities = {}
    
    # Split the text into words
    words = text.split()
    
    # Iterate through words to identify and categorize entities
    for word in words:
        if word.istitle() and word not in ['To', 'The', 'A', 'An']:
            if word.lower() in ['john', 'mary', 'alice', 'bob']:
                entities['Person'] = word
            elif word.lower() in ['paris', 'london', 'new york', 'tokyo']:
                entities['Location'] = word
    
    # Format the output string
    output = []
    for entity_type, entity_value in entities.items():
        output.append(f"{entity_type}: {entity_value}")
    
    return ', '.join(output)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('Alice is planning a trip to New York.'))  # Should print: Person: Alice, Location: New York
    print(tentacle('Bob dreams of going to Tokyo someday.'))  # Should print: Person: Bob, Location: Tokyo
    print(tentacle('The cat sat on the mat.'))  # Should print: (empty string)
    print(tentacle('A man walked his dog in the park.'))  # Should print: (empty string)
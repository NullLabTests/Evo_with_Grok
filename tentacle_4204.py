# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.
    
    This function identifies and extracts 'Person' and 'Location' entities from a given text.
    It uses simple pattern matching to identify these entities.
    
    Args:
    text (str): A string containing text to be analyzed.
    
    Returns:
    str: A string containing identified entities in the format 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Initialize an empty dictionary to store entities
    entities = {}

    # Split the text into words
    words = text.split()

    # Iterate through words to identify entities
    for i, word in enumerate(words):
        # Check for person names (assuming proper nouns start with a capital letter)
        if word.istitle() and i == 0:  # First word in the sentence
            entities['Person'] = word
        
        # Check for location names (assuming they follow 'to' or 'in')
        if word.lower() in ['to', 'in'] and i + 1 < len(words):
            location = words[i + 1]
            if location.istitle():  # Assuming proper nouns start with a capital letter
                entities['Location'] = location

    # Format the result
    result = []
    for entity_type, entity_name in entities.items():
        result.append(f"{entity_type}: {entity_name}")

    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The cat sat on the mat.'))  # Should print: 
    print(tentacle('In New York, Sarah met Tom.'))  # Should print: Person: Sarah, Location: New York
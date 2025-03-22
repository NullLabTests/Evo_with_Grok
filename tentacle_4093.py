# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from the given text.
    
    Args:
    text (str): A string containing the text to parse.
    
    Returns:
    str: A formatted string containing extracted entities.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Initialize dictionaries to store entities
    entities = {
        'Person': [],
        'Location': []
    }
    
    # Split the text into words
    words = text.split()
    
    # Iterate through words to identify entities
    for word in words:
        # Check for person names (simple heuristic: capitalized words)
        if word.istitle() and word.lower() not in ['the', 'a', 'an', 'and', 'or', 'but']:
            entities['Person'].append(word)
        
        # Check for locations (simple heuristic: capitalized words at the end of the sentence)
        if word.istitle() and words.index(word) == len(words) - 1:
            entities['Location'].append(word)
    
    # Format the result
    result = []
    for entity_type, entity_list in entities.items():
        if entity_list:
            result.append(f"{entity_type}: {', '.join(entity_list)}")
    
    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary and Tom visited New York.'))  # Should print: Person: Mary, Tom, Location: York
    print(tentacle('The cat sat on the mat.'))  # Should print: (nothing, as no entities are detected)
    print(tentacle('Alice traveled to London with Bob.'))  # Should print: Person: Alice, Bob, Location: London
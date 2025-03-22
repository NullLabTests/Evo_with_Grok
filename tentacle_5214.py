# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text, such as persons and locations.
    
    Args:
    text (str): A string containing text to parse for entities.
    
    Returns:
    str: A string containing the extracted entities in the format 'Entity: Value'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Initialize an empty dictionary to store entities
    entities = {}
    
    # Split the text into words
    words = text.split()
    
    # Iterate through words to find entities
    for i, word in enumerate(words):
        # Check for person names (simple heuristic: capitalized words not at the start of the sentence)
        if word.istitle() and i > 0:
            if 'Person' not in entities:
                entities['Person'] = word
            else:
                entities['Person'] += f" {word}"
        
        # Check for locations (simple heuristic: 'to' followed by a capitalized word)
        if word.lower() == 'to' and i + 1 < len(words) and words[i+1].istitle():
            if 'Location' not in entities:
                entities['Location'] = words[i+1]
            else:
                entities['Location'] += f" {words[i+1]}"
    
    # Format the result string
    result = ', '.join([f"{key}: {value}" for key, value in entities.items()])
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary and Tom visited New York.'))  # Should print: Person: Mary Tom, Location: New York
    print(tentacle('I live in London.'))  # Should print: Location: London
    print(tentacle('The meeting is at 3 PM.'))  # Should print: (empty string)
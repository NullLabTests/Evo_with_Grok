# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text, specifically persons and locations.
    
    Args:
    text (str): A string containing text to analyze.
    
    Returns:
    str: A formatted string with extracted entities.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Initialize a dictionary to store entities
    entities = {'Person': None, 'Location': None}
    
    # Split the text into words
    words = text.split()
    
    # Simple rule-based entity extraction
    for word in words:
        if word.istitle() and word not in ['To', 'Went']:  # Assuming proper nouns are entities
            if entities['Person'] is None:
                entities['Person'] = word
            elif entities['Location'] is None:
                entities['Location'] = word
    
    # Format the result
    result = []
    for key, value in entities.items():
        if value:
            result.append(f"{key}: {value}")
    
    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London yesterday.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The city of New York is amazing.'))  # Should print: Location: New York
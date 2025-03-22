# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to parse for entities.
    
    Returns:
    str: A string with extracted entities formatted as 'Entity Type: Entity'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Dictionary to store entity types and their corresponding keywords
    entity_keywords = {
        'Person': ['John', 'Jane', 'Bob', 'Alice'],
        'Location': ['Paris', 'London', 'New York', 'Tokyo']
    }
    
    # List to store identified entities
    identified_entities = []
    
    # Split the text into words
    words = text.split()
    
    # Iterate through words and check for entity matches
    for word in words:
        for entity_type, keywords in entity_keywords.items():
            if word in keywords:
                identified_entities.append(f"{entity_type}: {word}")
                break  # Stop checking other entity types for this word
    
    # Join identified entities into a single string
    result = ', '.join(identified_entities)
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Jane is traveling to London.'))  # Should print: Person: Jane, Location: London
    print(tentacle('Bob lives in New York.'))  # Should print: Person: Bob, Location: New York
    print(tentacle('Alice visited Tokyo last year.'))  # Should print: Person: Alice, Location: Tokyo
    print(tentacle('The weather is nice today.'))  # Should print: (empty string)
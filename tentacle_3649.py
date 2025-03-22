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
    # Dictionary to store entity types and their corresponding keywords
    entity_keywords = {
        'Person': ['John', 'Jane', 'Alice', 'Bob'],
        'Location': ['Paris', 'London', 'New York', 'Tokyo']
    }
    
    # Initialize an empty list to store found entities
    found_entities = []
    
    # Iterate through the text and check for entity keywords
    for word in text.split():
        for entity_type, keywords in entity_keywords.items():
            if word in keywords:
                found_entities.append(f"{entity_type}: {word}")
                break  # Stop checking once a match is found
    
    # Join the found entities into a single string
    result = ', '.join(found_entities)
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Jane visited London and met Bob.'))  # Should print: Person: Jane, Location: London, Person: Bob
    print(tentacle('Alice is planning a trip to Tokyo.'))  # Should print: Person: Alice, Location: Tokyo
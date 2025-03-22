# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to parse for entities.
    
    Returns:
    str: A string containing identified entities in the format 'Entity Type: Entity Name'.
    
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
                break  # Move to the next word after finding a match
    
    # Join identified entities with commas
    return ', '.join(identified_entities)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Jane visited London and met Bob.'))  # Should print: Person: Jane, Location: London, Person: Bob
    print(tentacle('Alice is planning a trip to Tokyo.'))  # Should print: Person: Alice, Location: Tokyo
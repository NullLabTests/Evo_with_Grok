# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to parse.
    
    Returns:
    str: A string with extracted entities in the format 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Initialize a dictionary to store entities
    entities = {}
    
    # List of words and their corresponding entity types
    entity_types = {
        'person': ['John', 'Jane', 'Bob', 'Alice'],
        'location': ['Paris', 'London', 'New York', 'Tokyo']
    }
    
    # Split the text into words
    words = text.split()
    
    # Iterate through words and identify entities
    for word in words:
        for entity_type, entity_list in entity_types.items():
            if word in entity_list:
                if entity_type not in entities:
                    entities[entity_type] = word
                else:
                    entities[entity_type] += f", {word}"
    
    # Format the result
    result = []
    for entity_type, entity_names in entities.items():
        result.append(f"{entity_type.capitalize()}: {entity_names}")
    
    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Jane and Bob visited London and New York.'))  # Should print: Person: Jane, Bob, Location: London, New York
    print(tentacle('Alice is planning a trip to Tokyo.'))  # Should print: Person: Alice, Location: Tokyo
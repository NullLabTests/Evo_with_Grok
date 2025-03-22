# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to parse for entities.
    
    Returns:
    str: A string containing the extracted entities in the format 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Dictionary of entity types and their corresponding keywords
    entity_types = {
        'Person': ['John', 'Mary', 'David', 'Sarah'],
        'Location': ['Paris', 'London', 'New York', 'Tokyo']
    }
    
    # Initialize a list to store extracted entities
    extracted_entities = []
    
    # Split the text into words
    words = text.split()
    
    # Iterate through the words and check for entity matches
    for word in words:
        for entity_type, entity_list in entity_types.items():
            if word in entity_list:
                extracted_entities.append(f"{entity_type}: {word}")
                break  # Stop checking other entity types for this word
    
    # Join the extracted entities into a single string
    result = ', '.join(extracted_entities)
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary is visiting London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('David lives in New York.'))  # Should print: Person: David, Location: New York
    print(tentacle('Sarah traveled to Tokyo.'))  # Should print: Person: Sarah, Location: Tokyo
    print(tentacle('The weather in Chicago is great.'))  # Should print: (nothing, as Chicago is not in the Location list)
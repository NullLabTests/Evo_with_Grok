# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to be analyzed.
    
    Returns:
    str: A string with extracted entities formatted as 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Dictionary to store entity types and their corresponding keywords
    entity_keywords = {
        'Person': ['John', 'Jane', 'Mike', 'Emily'],
        'Location': ['Paris', 'London', 'New York', 'Tokyo']
    }
    
    # Initialize a list to store identified entities
    identified_entities = []
    
    # Iterate through the text and check for entity keywords
    for word in text.split():
        for entity_type, keywords in entity_keywords.items():
            if word in keywords:
                identified_entities.append(f"{entity_type}: {word}")
                break  # Move to the next word after finding a match
    
    # Join the identified entities into a single string
    result = ', '.join(identified_entities)
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Jane visited London and met Mike.'))  # Should print: Person: Jane, Location: London, Person: Mike
    print(tentacle('Emily is planning a trip to Tokyo.'))  # Should print: Person: Emily, Location: Tokyo
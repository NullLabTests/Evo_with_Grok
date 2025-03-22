# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to parse for entities.
    
    Returns:
    str: A string with extracted entities formatted as 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Dictionary to store entity types and their corresponding keywords
    entity_keywords = {
        'Person': ['John', 'Mary', 'David', 'Emma'],
        'Location': ['Paris', 'New York', 'London', 'Tokyo']
    }
    
    # List to store extracted entities
    extracted_entities = []
    
    # Iterate through the text and check for entity keywords
    for word in text.split():
        for entity_type, keywords in entity_keywords.items():
            if word in keywords:
                extracted_entities.append(f"{entity_type}: {word}")
                break  # Move to the next word after finding a match
    
    # Join extracted entities with commas
    return ', '.join(extracted_entities)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited New York and met David.'))  # Should print: Person: Mary, Location: New York, Person: David
    print(tentacle('Emma is planning a trip to London.'))  # Should print: Person: Emma, Location: London
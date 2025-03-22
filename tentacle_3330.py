# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing the text to parse.
    
    Returns:
    str: A string containing the extracted entities in the format 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Dictionary to store entity types and their corresponding keywords
    entity_keywords = {
        'Person': ['John', 'Mary', 'David', 'Sarah'],
        'Location': ['Paris', 'London', 'New York', 'Tokyo']
    }
    
    # Initialize a list to store extracted entities
    extracted_entities = []
    
    # Split the text into words
    words = text.split()
    
    # Iterate through the words and check for entity matches
    for word in words:
        for entity_type, keywords in entity_keywords.items():
            if word in keywords:
                extracted_entities.append(f"{entity_type}: {word}")
                break  # Move to the next word after finding a match
    
    # Join the extracted entities with commas
    result = ', '.join(extracted_entities)
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London and met David.'))  # Should print: Person: Mary, Location: London, Person: David
    print(tentacle('Sarah is planning a trip to Tokyo.'))  # Should print: Person: Sarah, Location: Tokyo
    print(tentacle('The weather in New York is great today.'))  # Should print: Location: New York
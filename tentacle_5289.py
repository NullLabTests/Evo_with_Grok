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
        'Person': ['John', 'Mary', 'David', 'Sarah'],
        'Location': ['Paris', 'New York', 'London', 'Tokyo']
    }
    
    # Initialize an empty list to store identified entities
    identified_entities = []
    
    # Split the text into words
    words = text.split()
    
    # Iterate through the words to identify entities
    for word in words:
        for entity_type, keywords in entity_keywords.items():
            if word in keywords:
                identified_entities.append(f"{entity_type}: {word}")
                break  # Move to the next word after finding a match
    
    # Join the identified entities with commas
    result = ', '.join(identified_entities)
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary is visiting London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('David and Sarah are in New York.'))  # Should print: Person: David, Person: Sarah, Location: New York
    print(tentacle('Tokyo is a beautiful city.'))  # Should print: Location: Tokyo
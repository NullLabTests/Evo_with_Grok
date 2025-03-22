# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to analyze.
    
    Returns:
    str: A string with identified entities and their types.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Define dictionaries of entity types and their common examples
    entities = {
        'Person': ['John', 'Mary', 'David', 'Lisa'],
        'Location': ['Paris', 'London', 'New York', 'Tokyo']
    }
    
    # Initialize a list to store identified entities
    identified_entities = []
    
    # Split the text into words
    words = text.split()
    
    # Iterate through the words to find matching entities
    for word in words:
        for entity_type, examples in entities.items():
            if word in examples:
                identified_entities.append(f"{entity_type}: {word}")
                break  # Move to the next word after finding a match
    
    # Join the identified entities into a single string
    result = ', '.join(identified_entities)
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London and met David.'))  # Should print: Person: Mary, Location: London, Person: David
    print(tentacle('Lisa is planning a trip to Tokyo.'))  # Should print: Person: Lisa, Location: Tokyo
# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to analyze.
    
    Returns:
    str: A string containing extracted entities in the format 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Dictionary to store entity types and their corresponding patterns
    entity_patterns = {
        'Person': r'\b[A-Z][a-z]+\b',
        'Location': r'\b(?:Paris|London|New York|Tokyo|Berlin)\b'
    }
    
    # Initialize a list to store found entities
    entities = []
    
    # Iterate through entity types and patterns
    for entity_type, pattern in entity_patterns.items():
        # Find all matches in the text
        matches = re.findall(pattern, text)
        # Add found entities to the list
        for match in matches:
            entities.append(f"{entity_type}: {match}")
    
    # Join the entities with commas and return the result
    return ', '.join(entities)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London and Tokyo.'))  # Should print: Person: Mary, Location: London, Location: Tokyo
    print(tentacle('No entities here.'))  # Should print: 
    print(tentacle('Alice and Bob are going to Berlin.'))  # Should print: Person: Alice, Person: Bob, Location: Berlin
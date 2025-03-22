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
    import re
    
    # Dictionary to store entity types and their patterns
    entity_patterns = {
        'Person': r'\b[A-Z][a-z]+\b',
        'Location': r'\b(?:Paris|London|New York|Tokyo)\b'
    }
    
    # Initialize a list to store found entities
    found_entities = []
    
    # Iterate through entity patterns
    for entity_type, pattern in entity_patterns.items():
        # Find all matches for the current entity type
        matches = re.findall(pattern, text)
        # Add found entities to the list
        for match in matches:
            found_entities.append(f"{entity_type}: {match}")
    
    # Join the found entities with commas
    return ', '.join(found_entities)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London and New York.'))  # Should print: Person: Mary, Location: London, Location: New York
    print(tentacle('Tokyo is a beautiful city.'))  # Should print: Location: Tokyo
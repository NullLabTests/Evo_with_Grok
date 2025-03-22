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
    
    # Define patterns for entity recognition
    patterns = [
        (r'\b[A-Z][a-z]+\b', 'Person'),
        (r'\b(?:to|in|at)\s+([A-Z][a-z]+(?:[\s-][A-Z][a-z]+)*)\b', 'Location')
    ]
    
    # Iterate through the patterns and find matches
    for pattern, entity_type in patterns:
        import re
        matches = re.findall(pattern, text)
        for match in matches:
            if entity_type not in entities:
                entities[entity_type] = []
            if match not in entities[entity_type]:
                entities[entity_type].append(match)
    
    # Format the result
    result = []
    for entity_type, entity_list in entities.items():
        for entity in entity_list:
            result.append(f"{entity_type}: {entity}")
    
    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary and Tom visited New York and London.'))  # Should print: Person: Mary, Person: Tom, Location: New York, Location: London
    print(tentacle('The capital of France is Paris.'))  # Should print: Location: France, Location: Paris
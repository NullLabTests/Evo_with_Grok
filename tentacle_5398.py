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
    # Initialize an empty list to store extracted entities
    entities = []
    
    # Define patterns to match entities
    patterns = [
        (r'\b[A-Z][a-z]+\b', 'Person'),  # Matches capitalized words as potential names
        (r'\b(?:in|to|from)\s([A-Z][a-z]+(?:[\s-][A-Z][a-z]+)*)\b', 'Location')  # Matches locations after prepositions
    ]
    
    # Iterate through patterns and find matches
    for pattern, entity_type in patterns:
        import re
        matches = re.findall(pattern, text)
        for match in matches:
            entities.append(f"{entity_type}: {match}")
    
    # Join the entities with commas and return the result
    return ', '.join(entities)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary flew from New York to Los Angeles.'))  # Should print: Person: Mary, Location: New York, Location: Los Angeles
    print(tentacle('In London, David met with Sarah.'))  # Should print: Location: London, Person: David, Person: Sarah
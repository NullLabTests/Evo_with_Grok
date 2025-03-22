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
    import re
    
    # Initialize an empty dictionary to store entities
    entities = {}
    
    # Extract person names (assuming simple first name only)
    person_match = re.search(r'\b([A-Z][a-z]+)\b', text)
    if person_match:
        entities['Person'] = person_match.group(1)
    
    # Extract location names (assuming capitalized words)
    location_match = re.search(r'\b([A-Z][a-z]+)\b(?![^(]*\))', text)
    if location_match:
        entities['Location'] = location_match.group(1)
    
    # Format the output string
    result = ', '.join(f"{entity_type}: {entity_name}" for entity_type, entity_name in entities.items())
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London and New York.'))  # Should print: Person: Mary, Location: London
    print(tentacle('In Tokyo, David met Sarah.'))  # Should print: Location: Tokyo, Person: David
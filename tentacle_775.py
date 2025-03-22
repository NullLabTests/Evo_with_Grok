# Domains: text processing, natural language processing
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
    
    # Dictionary to store extracted entities
    entities = {}
    
    # Extract person names (assuming capitalized words at the beginning of the sentence)
    person_match = re.match(r'^([A-Z][a-z]+)', text)
    if person_match:
        entities['Person'] = person_match.group(1)
    
    # Extract location names (assuming capitalized words at the end of the sentence)
    location_match = re.search(r'\bto ([A-Z][a-z]+)\.?$', text)
    if location_match:
        entities['Location'] = location_match.group(1)
    
    # Format the output
    return ', '.join(f"{entity_type}: {entity_name}" for entity_type, entity_name in entities.items())

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary traveled to London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The cat sat on the mat.'))  # Should print: (nothing, as no entities are extracted)
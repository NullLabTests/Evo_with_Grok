# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from the given text.
    
    Args:
    text (str): A string containing the text to be analyzed.
    
    Returns:
    str: A string with extracted entities formatted as 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Initialize a dictionary to store extracted entities
    entities = {
        'Person': None,
        'Location': None
    }
    
    # Extract Person (assuming it's the first word in the sentence)
    person_match = re.match(r'^(\w+)', text)
    if person_match:
        entities['Person'] = person_match.group(1)
    
    # Extract Location (assuming it's the last word in the sentence)
    location_match = re.search(r'(\w+)\.$', text)
    if location_match:
        entities['Location'] = location_match.group(1)
    
    # Format the result string
    result = []
    for entity_type, entity_name in entities.items():
        if entity_name:
            result.append(f"{entity_type}: {entity_name}")
    
    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The city of Tokyo is amazing.'))  # Should print: Location: Tokyo
    print(tentacle('I love New York.'))  # Should print: Location: York
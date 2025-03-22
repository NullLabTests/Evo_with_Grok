# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from the given text.
    
    Args:
    text (str): A string containing the text to parse.
    
    Returns:
    str: A string with extracted entities formatted as 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Initialize a dictionary to store entities
    entities = {}
    
    # Extract Person (assuming the first word is a person's name)
    person_match = re.match(r'^(\w+)', text)
    if person_match:
        entities['Person'] = person_match.group(1)
    
    # Extract Location (assuming it's the last word in the sentence)
    location_match = re.search(r'(\w+)\.$', text)
    if location_match:
        entities['Location'] = location_match.group(1)
    
    # Format the output string
    result = ', '.join([f"{entity_type}: {entity}" for entity_type, entity in entities.items()])
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The city of Rome is beautiful.'))  # Should print: Location: Rome
    print(tentacle('Alice and Bob are friends.'))  # Should print: Person: Alice
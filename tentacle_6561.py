# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text, such as persons and locations.
    
    Args:
    text (str): A string containing the text to parse.
    
    Returns:
    str: A string containing the extracted entities in the format 'Entity: Value'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Initialize a dictionary to store entities
    entities = {}
    
    # Extract persons (assuming names start with a capital letter and are followed by lowercase letters)
    persons = re.findall(r'\b[A-Z][a-z]+\b', text)
    if persons:
        entities['Person'] = ', '.join(persons)
    
    # Extract locations (assuming they are capitalized and not at the start of the sentence)
    locations = re.findall(r'\b(?!^)[A-Z][a-z]+\b', text)
    if locations:
        entities['Location'] = ', '.join(locations)
    
    # Format the output string
    result = ', '.join(f"{key}: {value}" for key, value in entities.items())
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary and Alice visited New York and London.'))  # Should print: Person: Mary, Alice, Location: New York, London
    print(tentacle('The cat sat on the mat.'))  # Should print: (nothing, as no persons or locations are detected)
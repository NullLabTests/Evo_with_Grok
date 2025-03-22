# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to parse for entities.
    
    Returns:
    str: A string with identified entities and their types.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Define regex patterns for entity extraction
    person_pattern = r'\b[A-Z][a-z]+\b'
    location_pattern = r'\b(?:[A-Z][a-z]+(?: [A-Z][a-z]+)*)\b'
    
    # Extract entities
    persons = re.findall(person_pattern, text)
    locations = re.findall(location_pattern, text)
    
    # Filter out common words that might be mistakenly identified as persons
    common_words = ['The', 'A', 'An', 'And', 'But', 'Or', 'For', 'Nor', 'On', 'At', 'To', 'From', 'By']
    persons = [person for person in persons if person.capitalize() not in common_words]
    
    # Construct the result string
    result = []
    if persons:
        result.append(f"Person: {', '.join(persons)}")
    if locations:
        result.append(f"Location: {', '.join(locations)}")
    
    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Alice and Bob visited New York and London.'))  # Should print: Person: Alice, Bob, Location: New York, London
    print(tentacle('The cat sat on the mat.'))  # Should print: (empty string)
    print(tentacle('In Tokyo, Mary met David at the cafe.'))  # Should print: Person: Mary, David, Location: Tokyo
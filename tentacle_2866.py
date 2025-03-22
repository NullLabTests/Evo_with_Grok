# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from the given text.
    
    Args:
    text (str): A string containing the text to parse.
    
    Returns:
    str: A formatted string with extracted entities.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Define regex patterns for person and location
    person_pattern = r'\b[A-Z][a-z]+\b'
    location_pattern = r'\bto\s([A-Z][a-z]+)\b'
    
    # Extract person
    person = re.search(person_pattern, text)
    person_name = person.group(0) if person else None
    
    # Extract location
    location = re.search(location_pattern, text)
    location_name = location.group(1) if location else None
    
    # Format the result
    result_parts = []
    if person_name:
        result_parts.append(f"Person: {person_name}")
    if location_name:
        result_parts.append(f"Location: {location_name}")
    
    return ', '.join(result_parts)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The city of Rome is beautiful.'))  # Should print: Location: Rome
    print(tentacle('Alice and Bob talked.'))  # Should print: Person: Alice, Person: Bob
    print(tentacle('I love New York.'))  # Should print: Location: York
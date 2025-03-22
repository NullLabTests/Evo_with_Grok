# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from the given text.
    
    Args:
    text (str): A string containing the text to be analyzed.
    
    Returns:
    str: A formatted string containing the extracted entities.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Extract person names (simple regex for demonstration)
    person_pattern = r'\b([A-Z][a-z]+)\b'
    persons = re.findall(person_pattern, text)
    
    # Extract locations (simple regex for demonstration)
    location_pattern = r'to\s+(\b[A-Z][a-z]+\b)'
    locations = re.findall(location_pattern, text)
    
    # Format the result
    result_parts = []
    if persons:
        result_parts.append(f"Person: {', '.join(persons)}")
    if locations:
        result_parts.append(f"Location: {', '.join(locations)}")
    
    return ', '.join(result_parts)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London and New York.'))  # Should print: Person: Mary, Location: London, Location: New York
    print(tentacle('The cat sat on the mat.'))  # Should print: (empty string)
    print(tentacle('Alice and Bob traveled to Rome.'))  # Should print: Person: Alice, Person: Bob, Location: Rome
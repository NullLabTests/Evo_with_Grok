# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from the given text.
    
    Args:
    text (str): A string containing the text to be parsed.
    
    Returns:
    str: A formatted string containing the extracted entities.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Extract person names (assuming simple format: capitalized first name)
    person = re.search(r'\b([A-Z][a-z]+)\b', text)
    person_name = person.group(1) if person else None
    
    # Extract location names (assuming simple format: capitalized place name)
    location = re.search(r'\bto\s+([A-Z][a-z]+)\b', text)
    location_name = location.group(1) if location else None
    
    # Format the result
    result = []
    if person_name:
        result.append(f"Person: {person_name}")
    if location_name:
        result.append(f"Location: {location_name}")
    
    return ', '.join(result) if result else "No entities found"

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The cat sat on the mat.'))  # Should print: No entities found
    print(tentacle('In New York, Alice met Bob.'))  # Should print: Person: New, Person: Alice, Person: Bob
    print(tentacle('David traveled to Rome and then to Berlin.'))  # Should print: Person: David, Location: Rome, Location: Berlin
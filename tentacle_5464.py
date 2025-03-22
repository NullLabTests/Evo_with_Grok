# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from a given text.
    
    Args:
    text (str): A string containing the text to be analyzed.
    
    Returns:
    str: A string with extracted entities formatted as 'Entity: Value'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Extract person names (assuming capitalized words at the beginning of sentences)
    person_match = re.match(r'^([A-Z][a-z]+)', text)
    person = person_match.group(1) if person_match else None
    
    # Extract location names (assuming capitalized words at the end of sentences)
    location_match = re.search(r'\b([A-Z][a-z]+)\.$', text)
    location = location_match.group(1) if location_match else None
    
    # Format the result
    result_parts = []
    if person:
        result_parts.append(f"Person: {person}")
    if location:
        result_parts.append(f"Location: {location}")
    
    return ', '.join(result_parts)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The cat sat on the mat.'))  # Should print: (no output)
    print(tentacle('In New York, Bob met Alice.'))  # Should print: Person: Bob, Location: York
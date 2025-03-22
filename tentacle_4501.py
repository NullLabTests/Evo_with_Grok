# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from the given text.
    
    Args:
    text (str): A string containing the text to parse.
    
    Returns:
    str: A string containing the extracted entities in the format 'Person: <name>, Location: <place>'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Initialize variables to store extracted entities
    person = None
    location = None
    
    # Extract person (assuming the first word is a person's name)
    person_match = re.match(r'^([A-Z][a-z]+)\b', text)
    if person_match:
        person = person_match.group(1)
    
    # Extract location (assuming it's the last word in the sentence)
    location_match = re.search(r'\b([A-Z][a-z]+)\.$', text)
    if location_match:
        location = location_match.group(1)
    
    # Format and return the result
    result = []
    if person:
        result.append(f"Person: {person}")
    if location:
        result.append(f"Location: {location}")
    
    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The city of New York is amazing.'))  # Should print: Location: York
    print(tentacle('I love traveling.'))  # Should print: (empty string)
    print(tentacle('Alice and Bob went to Rome.'))  # Should print: Person: Alice, Location: Rome
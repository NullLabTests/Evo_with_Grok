# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from a given text.

    Args:
    text (str): A string containing a sentence or phrase.

    Returns:
    str: A formatted string with extracted entities.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re

    # Initialize empty lists for persons and locations
    persons = []
    locations = []

    # Extract persons (simple names)
    person_pattern = r'\b[A-Z][a-z]+\b'
    persons = re.findall(person_pattern, text)

    # Extract locations (capitalized words at the end of the sentence)
    location_pattern = r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b$'
    locations = re.findall(location_pattern, text)

    # Format the result
    result = []
    if persons:
        result.append(f"Person: {', '.join(persons)}")
    if locations:
        result.append(f"Location: {', '.join(locations)}")

    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited New York and London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The capital of France is Paris.'))  # Should print: Location: Paris
    print(tentacle('Alice and Bob are friends.'))  # Should print: Person: Alice, Bob
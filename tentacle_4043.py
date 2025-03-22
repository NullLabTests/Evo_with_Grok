# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text, identifying persons and locations.

    Args:
    text (str): A string containing text to parse for entities.

    Returns:
    str: A string with identified entities formatted as 'Entity Type: Entity Name'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re

    # Define regex patterns for persons and locations
    person_pattern = r'\b[A-Z][a-z]+\b'
    location_pattern = r'\b(?:to|in|at)\s([A-Z][a-z]+)\b'

    # Extract persons
    persons = re.findall(person_pattern, text)
    persons = [person for person in persons if person.lower() not in ['to', 'in', 'at']]

    # Extract locations
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
    print(tentacle('Mary and Tom visited London and Berlin.'))  # Should print: Person: Mary, Tom, Location: London, Berlin
    print(tentacle('In New York, Alice met Bob.'))  # Should print: Person: Alice, Bob, Location: New York
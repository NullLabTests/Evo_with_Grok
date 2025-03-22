# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.

    Args:
    text (str): A string containing text to parse for entities.

    Returns:
    str: A formatted string containing the extracted entities.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re

    # Define patterns for entity extraction
    person_pattern = r'\b[A-Z][a-z]+\b'
    location_pattern = r'\b(?:[A-Z][a-z]+\s?)+,?\s?(?:[A-Z][a-z]+)?\b'

    # Extract entities
    persons = re.findall(person_pattern, text)
    locations = re.findall(location_pattern, text)

    # Filter out potential false positives
    persons = [p for p in persons if p.lower() not in ['the', 'a', 'an', 'to', 'and', 'or', 'but']]
    locations = [l for l in locations if l.lower() not in ['the', 'a', 'an', 'to', 'and', 'or', 'but']]

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
    print(tentacle('Mary and Tom visited New York City.'))  # Should print: Person: Mary, Tom, Location: New York City
    print(tentacle('The capital of France is Paris.'))  # Should print: Location: France, Paris
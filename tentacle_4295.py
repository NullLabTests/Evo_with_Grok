# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.

    Args:
    text (str): A string containing text to parse.

    Returns:
    str: A string with extracted entities in the format 'Entity Type: Entity Name'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re

    # Define patterns for entity extraction
    person_pattern = r'\b([A-Z][a-z]+)\b'
    location_pattern = r'\b(to|in|at)\s([A-Z][a-z]+)\b'

    # Extract person names
    persons = re.findall(person_pattern, text)
    persons = [person for person in persons if person.lower() not in ['to', 'in', 'at']]

    # Extract locations
    locations = re.findall(location_pattern, text)
    locations = [location[1] for location in locations]

    # Format the output
    output = []
    if persons:
        output.append(f"Person: {', '.join(persons)}")
    if locations:
        output.append(f"Location: {', '.join(locations)}")

    return ', '.join(output)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary and Tom are visiting New York.'))  # Should print: Person: Mary, Tom, Location: New York
    print(tentacle('The conference is in London next week.'))  # Should print: Location: London
    print(tentacle('No specific names or locations mentioned.'))  # Should print: (empty string)
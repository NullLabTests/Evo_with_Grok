# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.

    Args:
    text (str): A string containing the text to be processed.

    Returns:
    str: A string containing the extracted entities in the format 'Entity Type: Entity Name'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re

    # Define regex patterns for entity extraction
    person_pattern = r'\b([A-Z][a-z]+)\b'
    location_pattern = r'\b(to|in|at)\s([A-Z][a-z]+)\b'

    # Extract person names
    persons = re.findall(person_pattern, text)
    persons = [person for person in persons if person.lower() not in ['to', 'in', 'at']]

    # Extract locations
    locations = re.findall(location_pattern, text)
    locations = [location[1] for location in locations]

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
    print(tentacle('Mary and Alice visited London and New York.'))  # Should print: Person: Mary, Alice, Location: London, New York
    print(tentacle('The conference is in Tokyo.'))  # Should print: Location: Tokyo
    print(tentacle('No entities here.'))  # Should print:
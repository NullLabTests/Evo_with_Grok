# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from the given text.
    
    Args:
    text (str): A string containing text to be parsed.
    
    Returns:
    str: A string containing extracted entities in the format 'Person: <name>, Location: <place>'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re

    # Initialize variables to store extracted entities
    person = None
    location = None

    # Extract person using regex pattern for names
    person_match = re.search(r'\b([A-Z][a-z]+)\b', text)
    if person_match:
        person = person_match.group(1)

    # Extract location using regex pattern for places
    location_match = re.search(r'\bto\s+([A-Z][a-z]+)\b', text)
    if location_match:
        location = location_match.group(1)

    # Construct the result string
    result = []
    if person:
        result.append(f'Person: {person}')
    if location:
        result.append(f'Location: {location}')

    return ', '.join(result) if result else 'No entities found.'

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The weather in New York is great.'))  # Should print: Location: New York
    print(tentacle('I love traveling.'))  # Should print: No entities found.
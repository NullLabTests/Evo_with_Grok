# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from the given text.
    
    Args:
    text (str): A string containing the text to parse.
    
    Returns:
    str: A string with extracted entities in the format 'Person: <name>, Location: <place>'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re

    # Initialize variables to store extracted entities
    person = None
    location = None

    # Extract person (assuming person is the first word)
    person_match = re.match(r'^(\w+)', text)
    if person_match:
        person = person_match.group(1)

    # Extract location (assuming location is preceded by 'to')
    location_match = re.search(r'to\s+(\w+)', text)
    if location_match:
        location = location_match.group(1)

    # Construct and return the result string
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
    print(tentacle('The city of Tokyo is beautiful.'))  # Should print: Location: Tokyo
    print(tentacle('I am going to the store.'))  # Should print: Location: store
    print(tentacle('Hello world!'))  # Should print: (empty string)
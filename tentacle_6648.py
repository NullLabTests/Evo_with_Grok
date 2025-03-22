# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from the given text.

    Args:
    text (str): A string containing text to parse.

    Returns:
    str: A string containing extracted entities in the format 'Entity: Value'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re

    # Initialize variables to store extracted entities
    person = None
    location = None

    # Extract person using regex (assuming person is a single word at the beginning)
    person_match = re.match(r'^(\w+)', text)
    if person_match:
        person = person_match.group(1)

    # Extract location using regex (assuming location is a single word at the end)
    location_match = re.search(r'(\w+)\.$', text)
    if location_match:
        location = location_match.group(1)

    # Construct the result string
    result = []
    if person:
        result.append(f"Person: {person}")
    if location:
        result.append(f"Location: {location}")

    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Alice visited London.'))  # Should print: Person: Alice, Location: London
    print(tentacle('Bob is in New York.'))  # Should print: Person: Bob, Location: York
    print(tentacle('Mary likes Tokyo.'))  # Should print: Person: Mary, Location: Tokyo
    print(tentacle('David explored Rome.'))  # Should print: Person: David, Location: Rome
    print(tentacle('Sarah went to Berlin.'))  # Should print: Person: Sarah, Location: Berlin
    print(tentacle('Michael is from Sydney.'))  # Should print: Person: Michael, Location: Sydney
    print(tentacle('Emma visited Los Angeles.'))  # Should print: Person: Emma, Location: Angeles
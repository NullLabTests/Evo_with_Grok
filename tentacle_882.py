# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from a given text.

    Args:
    text (str): A string containing text to parse for entities.

    Returns:
    str: A string containing identified entities in the format 'Entity: Value'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re

    # Initialize dictionaries to store entities
    entities = {'Person': '', 'Location': ''}

    # Extract Person entity
    person_match = re.search(r'\b([A-Z][a-z]+)\b', text)
    if person_match:
        entities['Person'] = person_match.group(1)

    # Extract Location entity
    location_match = re.search(r'\bto\s([A-Z][a-zA-Z]+)\b', text)
    if location_match:
        entities['Location'] = location_match.group(1)

    # Format the result
    result = ', '.join([f"{key}: {value}" for key, value in entities.items() if value])
    return result if result else "No entities found."

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited New York.'))  # Should print: Person: Mary, Location: New York
    print(tentacle('The weather in London is great.'))  # Should print: Location: London
    print(tentacle('Just a random sentence.'))  # Should print: No entities found.
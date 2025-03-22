# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.

    This function identifies and extracts 'Person' and 'Location' entities from a given text.
    It uses simple pattern matching to identify these entities.

    Args:
    text (str): A string containing text to analyze.

    Returns:
    str: A string with identified entities formatted as 'Entity: Value'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re

    # Initialize an empty dictionary to store identified entities
    entities = {}

    # Extract Person entity (assuming it's the first word in the sentence)
    person_match = re.match(r'^([A-Z][a-z]+)\b', text)
    if person_match:
        entities['Person'] = person_match.group(1)

    # Extract Location entity (assuming it's the last word in the sentence)
    location_match = re.search(r'\b([A-Z][a-z]+)\.$', text)
    if location_match:
        entities['Location'] = location_match.group(1)

    # Format the result string
    result = ', '.join([f"{entity}: {value}" for entity, value in entities.items()])

    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The cat sat on the mat.'))  # Should print: (empty string)
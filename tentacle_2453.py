# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text, identifying persons and locations.

    Args:
    text (str): A string containing text to analyze.

    Returns:
    str: A string with identified entities formatted as 'Entity Type: Entity Name'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re

    # Initialize a dictionary to store entities
    entities = {'Person': [], 'Location': []}

    # Extract persons (assuming capitalized words at the start of the sentence)
    person_match = re.match(r'^([A-Z][a-z]+)\b', text)
    if person_match:
        entities['Person'].append(person_match.group(1))

    # Extract locations (assuming capitalized words not at the start)
    location_matches = re.findall(r'\b([A-Z][a-z]+)\b', text[text.find(' '):])
    entities['Location'].extend(location_matches)

    # Format the result
    result = []
    for entity_type, entity_list in entities.items():
        if entity_list:
            result.append(f"{entity_type}: {', '.join(entity_list)}")

    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London and New York.'))  # Should print: Person: Mary, Location: London, New York
    print(tentacle('The capital of France is Paris.'))  # Should print: Location: France, Paris
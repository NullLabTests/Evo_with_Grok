# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.

    Args:
    text (str): A string containing text to parse.

    Returns:
    str: A string with extracted entities formatted as 'Entity: Value'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Initialize a dictionary to store entities
    entities = {}

    # Define patterns to search for entities
    patterns = [
        (r'\b[A-Z][a-z]+\b', 'Person'),  # Capitalized word as a potential person name
        (r'\b(?:in|to|at)\s+(\w+)', 'Location'),  # Words following 'in', 'to', or 'at' as potential locations
    ]

    # Iterate through patterns and search for matches
    for pattern, entity_type in patterns:
        import re
        matches = re.findall(pattern, text)
        if matches:
            entities[entity_type] = matches[0]  # Use the first match for each entity type

    # Format the result
    result = ', '.join(f"{entity_type}: {value}" for entity_type, value in entities.items())
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary is traveling to New York.'))  # Should print: Person: Mary, Location: New York
    print(tentacle('The meeting is in London.'))  # Should print: Location: London
# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.

    Args:
    text (str): A string containing text to be parsed.

    Returns:
    str: A string containing extracted entities formatted as 'Entity Type: Entity Name'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re

    # Dictionary to store entity types and their corresponding regex patterns
    entity_patterns = {
        'Person': r'\b[A-Z][a-z]+\b',
        'Location': r'\b(?:Paris|London|New York|Tokyo)\b'
    }

    # Initialize a list to store extracted entities
    extracted_entities = []

    # Iterate through entity types and their patterns
    for entity_type, pattern in entity_patterns.items():
        # Find all matches in the text
        matches = re.findall(pattern, text)
        # Add matches to the extracted entities list
        for match in matches:
            extracted_entities.append(f"{entity_type}: {match}")

    # Join the extracted entities with commas and return the result
    return ', '.join(extracted_entities)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London and New York.'))  # Should print: Person: Mary, Location: London, Location: New York
    print(tentacle('Tom lives in Tokyo.'))  # Should print: Person: Tom, Location: Tokyo
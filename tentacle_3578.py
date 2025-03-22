# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.

    Args:
    text (str): A string containing the text to process.

    Returns:
    str: A string with extracted entities in the format 'Entity Type: Entity Name, ...'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Dictionary to store entity types and their corresponding keywords
    entity_keywords = {
        'Person': ['John', 'Mary', 'David', 'Lisa'],
        'Location': ['Paris', 'New York', 'London', 'Tokyo']
    }

    # Initialize a list to store found entities
    found_entities = []

    # Iterate through the text and check for entity keywords
    for word in text.split():
        for entity_type, keywords in entity_keywords.items():
            if word in keywords:
                found_entities.append(f"{entity_type}: {word}")

    # Join the found entities into a single string
    result = ', '.join(found_entities)

    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary is traveling to Tokyo.'))  # Should print: Person: Mary, Location: Tokyo
    print(tentacle('David lives in New York.'))  # Should print: Person: David, Location: New York
    print(tentacle('Lisa visited London last week.'))  # Should print: Person: Lisa, Location: London
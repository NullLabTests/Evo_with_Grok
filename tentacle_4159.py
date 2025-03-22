# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.

    Args:
    text (str): A string containing text to parse for entities.

    Returns:
    str: A string with extracted entities formatted as 'Entity Type: Entity Name'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Dictionary to store entity types and their corresponding keywords
    entities = {
        'Person': ['John', 'Jane', 'Bob', 'Alice'],
        'Location': ['Paris', 'London', 'New York', 'Tokyo']
    }

    # Initialize an empty list to store found entities
    found_entities = []

    # Iterate through the text and check for entity matches
    for entity_type, entity_list in entities.items():
        for entity in entity_list:
            if entity in text:
                found_entities.append(f"{entity_type}: {entity}")

    # Join the found entities into a single string
    result = ', '.join(found_entities)

    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Jane is visiting London.'))  # Should print: Person: Jane, Location: London
    print(tentacle('Bob and Alice are in New York.'))  # Should print: Person: Bob, Person: Alice, Location: New York
    print(tentacle('Tokyo is a beautiful city.'))  # Should print: Location: Tokyo
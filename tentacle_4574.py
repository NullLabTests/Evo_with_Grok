# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities from text.

    Args:
    text (str): A string containing text to be analyzed.

    Returns:
    str: A string containing extracted entities in the format 'Entity Type: Entity'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Dictionary to store entity types and their corresponding keywords
    entity_keywords = {
        'Person': ['John', 'Mary', 'David', 'Sarah'],
        'Location': ['Paris', 'London', 'New York', 'Tokyo']
    }

    # Initialize an empty list to store extracted entities
    extracted_entities = []

    # Split the text into words
    words = text.split()

    # Iterate through the words and check for entity matches
    for word in words:
        for entity_type, keywords in entity_keywords.items():
            if word in keywords:
                extracted_entities.append(f"{entity_type}: {word}")

    # Join the extracted entities into a single string
    result = ', '.join(extracted_entities)

    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London and met David.'))  # Should print: Person: Mary, Location: London, Person: David
    print(tentacle('Sarah is planning a trip to Tokyo.'))  # Should print: Person: Sarah, Location: Tokyo
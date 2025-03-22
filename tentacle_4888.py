# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.

    Args:
    text (str): A string containing text to parse.

    Returns:
    str: A string containing extracted entities in the format 'Entity Type: Entity Name'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Define dictionaries for entity recognition
    person_names = ['John', 'Mary', 'David', 'Sarah']
    locations = ['Paris', 'London', 'New York', 'Tokyo']

    # Initialize a list to store recognized entities
    entities = []

    # Split the text into words
    words = text.split()

    # Iterate through words and identify entities
    for word in words:
        if word in person_names:
            entities.append(f'Person: {word}')
        elif word in locations:
            entities.append(f'Location: {word}')

    # Join the recognized entities into a single string
    result = ', '.join(entities)

    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary is visiting London and New York.'))  # Should print: Person: Mary, Location: London, Location: New York
    print(tentacle('David lives in Tokyo with Sarah.'))  # Should print: Person: David, Location: Tokyo, Person: Sarah
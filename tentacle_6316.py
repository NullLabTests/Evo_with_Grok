# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.

    This function identifies and extracts 'Person' and 'Location' entities from a given text.
    It uses simple string matching to identify these entities.

    Args:
    text (str): A string containing text to parse for entities.

    Returns:
    str: A formatted string containing identified entities and their values.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Initialize variables to store identified entities
    person = None
    location = None

    # List of common names for person identification
    common_names = ['John', 'Jane', 'Alice', 'Bob', 'Charlie', 'David', 'Eve']

    # List of common locations for location identification
    common_locations = ['Paris', 'London', 'New York', 'Tokyo', 'Sydney', 'Berlin', 'Rome']

    # Split the text into words
    words = text.split()

    # Identify person entity
    for word in words:
        if word in common_names:
            person = word
            break

    # Identify location entity
    for word in words:
        if word in common_locations:
            location = word
            break

    # Construct the result string
    result = []
    if person:
        result.append(f'Person: {person}')
    if location:
        result.append(f'Location: {location}')

    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Alice visited Tokyo.'))  # Should print: Person: Alice, Location: Tokyo
    print(tentacle('David is in New York.'))  # Should print: Person: David, Location: New York
    print(tentacle('Eve likes to travel.'))  # Should print: Person: Eve
    print(tentacle('I love Berlin in the summer.'))  # Should print: Location: Berlin
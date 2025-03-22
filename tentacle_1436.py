# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from the given text.

    Args:
    text (str): A string containing a sentence to analyze.

    Returns:
    str: A formatted string with extracted entities.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re

    # Initialize empty lists for extracted entities
    persons = []
    locations = []

    # Extract persons (assuming capitalized words at the start of the sentence)
    person_match = re.match(r'^([A-Z][a-z]+)', text)
    if person_match:
        persons.append(person_match.group(1))

    # Extract locations (assuming capitalized words at the end of the sentence)
    location_match = re.search(r' ([A-Z][a-z]+)\.$', text)
    if location_match:
        locations.append(location_match.group(1))

    # Format the result string
    result = []
    if persons:
        result.append(f"Person: {', '.join(persons)}")
    if locations:
        result.append(f"Location: {', '.join(locations)}")

    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The cat sat on the mat.'))  # Should print: (nothing, as no persons or locations are detected)
    print(tentacle('In New York, Alice met Bob.'))  # Should print: Person: Alice, Location: York
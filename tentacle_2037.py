# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from a given text.

    Args:
    text (str): A string containing a sentence or phrase.

    Returns:
    str: A formatted string containing extracted entities.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re

    # Initialize variables to store extracted entities
    person = None
    location = None

    # Extract person (assuming it's the first word in the sentence)
    person_match = re.match(r'^([A-Z][a-z]+)\b', text)
    if person_match:
        person = person_match.group(1)

    # Extract location (assuming it's the last word in the sentence)
    location_match = re.search(r'\b([A-Z][a-z]+)\.$', text)
    if location_match:
        location = location_match.group(1)

    # Format and return the result
    result_parts = []
    if person:
        result_parts.append(f"Person: {person}")
    if location:
        result_parts.append(f"Location: {location}")

    return ", ".join(result_parts) if result_parts else "No entities found."

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The cat sat on the mat.'))  # Should print: No entities found.
    print(tentacle('Alice and Bob traveled to Rome.'))  # Should print: Person: Alice, Location: Rome
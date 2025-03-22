# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text, identifying persons and locations.

    Args:
    text (str): A string containing text to parse for entities.

    Returns:
    str: A formatted string with identified entities.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import spacy

    # Load the English language model
    nlp = spacy.load("en_core_web_sm")

    # Process the text
    doc = nlp(text)

    persons = []
    locations = []

    # Iterate over entities in the text
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            persons.append(ent.text)
        elif ent.label_ == "GPE":  # Geo-Political Entity, typically used for cities and countries
            locations.append(ent.text)

    # Format the output
    result = []
    if persons:
        result.append(f"Person: {', '.join(persons)}")
    if locations:
        result.append(f"Location: {', '.join(locations)}")

    return ', '.join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Jane visited New York and met with Mark.'))  # Should print: Person: Jane, Mark, Location: New York
    print(tentacle('The capital of France is Paris.'))  # Should print: Location: France, Paris
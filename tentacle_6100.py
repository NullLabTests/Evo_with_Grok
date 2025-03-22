# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text, identifying persons and locations.

    Args:
    text (str): A string containing the text to be analyzed.

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

    # Initialize variables to store entities
    person = ""
    location = ""

    # Iterate over entities in the document
    for ent in doc.ents:
        if ent.label_ == "PERSON" and not person:
            person = ent.text
        elif ent.label_ == "GPE" and not location:  # GPE stands for Geo-Political Entity
            location = ent.text

    # Format the result
    result = []
    if person:
        result.append(f"Person: {person}")
    if location:
        result.append(f"Location: {location}")

    return ", ".join(result) if result else "No entities found."

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited New York.'))  # Should print: Person: Mary, Location: New York
    print(tentacle('The capital of France is Paris.'))  # Should print: Location: France, Location: Paris
    print(tentacle('The weather is nice today.'))  # Should print: No entities found.
# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.

    Args:
    text (str): A string containing text to parse for entities.

    Returns:
    str: A formatted string containing extracted entities.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import spacy

    # Load the English language model
    nlp = spacy.load("en_core_web_sm")

    # Process the text
    doc = nlp(text)

    # Extract entities
    entities = []
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            entities.append(f"Person: {ent.text}")
        elif ent.label_ == "GPE":
            entities.append(f"Location: {ent.text}")

    # Return formatted string of entities
    return ", ".join(entities)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited New York.'))  # Should print: Person: Mary, Location: New York
    print(tentacle('The capital of France is Paris.'))  # Should print: Location: France, Location: Paris
# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.

    Args:
    text (str): A string containing text to parse.

    Returns:
    str: A string with identified entities formatted as 'Entity Type: Entity Name'.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import spacy

    # Load the English language model
    nlp = spacy.load("en_core_web_sm")

    # Process the text
    doc = nlp(text)

    entities = []
    for ent in doc.ents:
        # Extract entity type and text
        entity_type = ent.label_
        entity_text = ent.text

        # Map entity types to more readable labels
        if entity_type == "PERSON":
            entities.append(f"Person: {entity_text}")
        elif entity_type == "GPE":
            entities.append(f"Location: {entity_text}")
        elif entity_type == "ORG":
            entities.append(f"Organization: {entity_text}")
        elif entity_type == "DATE":
            entities.append(f"Date: {entity_text}")

    # Join the extracted entities
    return ", ".join(entities)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Apple Inc. was founded on April 1, 1976, by Steve Jobs in Cupertino.'))  # Should print: Organization: Apple Inc., Date: April 1, 1976, Person: Steve Jobs, Location: Cupertino

# Note: This function requires the spaCy library and the English language model to be installed.
# You can install them using: pip install spacy && python -m spacy download en_core_web_sm
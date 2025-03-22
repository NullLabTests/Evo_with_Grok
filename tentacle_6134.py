# Domains: text processing, natural language processing
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
    import spacy

    # Load the English language model
    nlp = spacy.load("en_core_web_sm")

    # Process the text
    doc = nlp(text)

    # Extract entities
    entities = []
    for ent in doc.ents:
        if ent.label_ in ['PERSON', 'LOC', 'GPE']:
            entities.append(f"{ent.label_}: {ent.text}")

    # Join the entities into a single string
    return ', '.join(entities)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited New York last summer.'))  # Should print: Person: Mary, GPE: New York
    print(tentacle('The company is headquartered in Tokyo.'))  # Should print: GPE: Tokyo
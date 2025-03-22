# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.

    Args:
    text (str): A string containing text to parse.

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

    # Initialize a list to store extracted entities
    entities = []

    # Iterate through the recognized entities
    for ent in doc.ents:
        # Format the entity as 'Entity Type: Entity Name'
        entity_str = f"{ent.label_}: {ent.text}"
        entities.append(entity_str)

    # Join the entities with commas
    return ", ".join(entities)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('The company Apple was founded by Steve Jobs in Cupertino.'))  # Should print: Organization: Apple, Person: Steve Jobs, Location: Cupertino

# Note: This function requires the spaCy library and the English language model to be installed.
# You can install them using: pip install spacy && python -m spacy download en_core_web_sm
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
    import spacy

    # Load the English language model
    nlp = spacy.load("en_core_web_sm")

    # Process the text
    doc = nlp(text)

    # Initialize a list to store extracted entities
    entities = []

    # Iterate through the recognized entities
    for ent in doc.ents:
        # Extract entity type and text
        entity_type = ent.label_
        entity_text = ent.text

        # Format the entity information
        entity_info = f"{entity_type}: {entity_text}"

        # Add to the list of entities
        entities.append(entity_info)

    # Join the entities with commas and return the result
    return ", ".join(entities)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('The Eiffel Tower is in France.'))  # Should print: LOCATION: France, FACILITY: Eiffel Tower
    print(tentacle('Bill Gates founded Microsoft in 1975.'))  # Should print: PERSON: Bill Gates, ORG: Microsoft, DATE: 1975

# Note: To run this code, you need to install spaCy and download the English language model:
# pip install spacy
# python -m spacy download en_core_web_sm
# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.

    Args:
    text (str): A string containing text to parse for entities.

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

    # Iterate through the entities in the document
    for ent in doc.ents:
        # Append the entity type and text to the list
        entities.append(f"{ent.label_}: {ent.text}")

    # Join the entities with commas and return the result
    return ", ".join(entities)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('The Eiffel Tower is in Paris, France.'))  # Should print: LOCATION: Paris, GPE: France
    print(tentacle('Apple Inc. was founded by Steve Jobs.'))  # Should print: ORG: Apple Inc., PERSON: Steve Jobs
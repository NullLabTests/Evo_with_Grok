# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.

    Args:
    text (str): A string containing text to parse for entities.

    Returns:
    str: A string with identified entities and their types.

    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import spacy

    # Load the English language model
    nlp = spacy.load("en_core_web_sm")

    # Process the text
    doc = nlp(text)

    # Initialize a list to store identified entities
    entities = []

    # Iterate through the identified entities
    for ent in doc.ents:
        # Append the entity type and text to the list
        entities.append(f"{ent.label_}: {ent.text}")

    # Join the entities into a single string separated by commas
    result = ", ".join(entities)

    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('The Eiffel Tower is in Paris.'))  # Should print: Location: Paris
    print(tentacle('Apple Inc. was founded by Steve Jobs.'))  # Should print: Organization: Apple Inc., Person: Steve Jobs
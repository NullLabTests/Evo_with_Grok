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
    
    entities = []
    for ent in doc.ents:
        # Extract entity type and name
        entity_type = ent.label_
        entity_name = ent.text
        
        # Map entity types to more readable labels
        if entity_type == "PERSON":
            entities.append(f"Person: {entity_name}")
        elif entity_type == "GPE":
            entities.append(f"Location: {entity_name}")
        elif entity_type == "ORG":
            entities.append(f"Organization: {entity_name}")
        elif entity_type == "DATE":
            entities.append(f"Date: {entity_name}")
    
    # Join extracted entities into a single string
    return ", ".join(entities)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Apple Inc. was founded on April 1, 1976 by Steve Jobs.'))  # Should print: Organization: Apple Inc., Date: April 1, 1976, Person: Steve Jobs
    print(tentacle('The conference will be held in New York next month.'))  # Should print: Location: New York
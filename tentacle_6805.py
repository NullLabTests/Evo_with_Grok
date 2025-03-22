# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing text to parse for entities.
    
    Returns:
    str: A string with extracted entities and their types.
    
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
        # Extract entity text and label
        entity_text = ent.text
        entity_label = ent.label_
        
        # Convert label to a more readable format
        if entity_label == "PERSON":
            entity_type = "Person"
        elif entity_label == "GPE":
            entity_type = "Location"
        elif entity_label == "ORG":
            entity_type = "Organization"
        else:
            entity_type = entity_label
        
        entities.append(f"{entity_type}: {entity_text}")
    
    # Join the extracted entities
    result = ", ".join(entities)
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Apple Inc. is headquartered in Cupertino.'))  # Should print: Organization: Apple Inc., Location: Cupertino
    print(tentacle('The Eiffel Tower is in Paris, France.'))  # Should print: Location: Paris, Location: France
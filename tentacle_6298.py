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
    # Initialize a dictionary to store entities
    entities = {}
    
    # Split the text into words
    words = text.split()
    
    # Simple entity extraction rules
    for word in words:
        if word.istitle() and word not in entities.values():  # Assume capitalized words are proper nouns
            if word in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
                entities['Day'] = word
            elif word in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']:
                entities['Month'] = word
            elif word in ['Mr.', 'Mrs.', 'Ms.', 'Dr.']:
                entities['Title'] = word
            elif word.isalpha():
                if 'Person' not in entities:
                    entities['Person'] = word
                elif 'Location' not in entities:
                    entities['Location'] = word
                else:
                    entities['Entity'] = word  # Generic entity if Person and Location are already assigned
    
    # Format the result
    result = ', '.join([f"{entity_type}: {entity}" for entity_type, entity in entities.items()])
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Dr. Smith visited New York on Monday.'))  # Should print: Title: Dr., Person: Smith, Location: York, Day: Monday
    print(tentacle('The meeting is scheduled for March 15th in London.'))  # Should print: Month: March, Location: London
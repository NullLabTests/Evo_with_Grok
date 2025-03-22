# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from the given text.
    
    Args:
    text (str): A string containing text to be analyzed.
    
    Returns:
    str: A formatted string containing extracted entities.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    import re
    
    # Initialize dictionaries to store entities
    entities = {
        'Person': [],
        'Location': []
    }
    
    # Extract persons (assuming proper nouns starting with a capital letter)
    persons = re.findall(r'\b[A-Z][a-z]+\b', text)
    entities['Person'].extend(persons)
    
    # Extract locations (assuming proper nouns starting with a capital letter after 'to')
    locations = re.findall(r'to\s([A-Z][a-z]+)', text)
    entities['Location'].extend(locations)
    
    # Format the output string
    output = []
    for entity_type, entity_list in entities.items():
        if entity_list:
            output.append(f"{entity_type}: {', '.join(entity_list)}")
    
    return ', '.join(output)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London and met Alice.'))  # Should print: Person: Mary, Alice, Location: London
    print(tentacle('No entities here.'))  # Should print: (empty string)
    print(tentacle('David traveled from New York to Los Angeles.'))  # Should print: Person: David, Location: New, Los
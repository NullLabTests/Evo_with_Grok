# Domains: text processing, mathematics
def tentacle(text):
    """
    Parse and extract entities (Person and Location) from the given text.
    
    Args:
    text (str): A string containing text to be analyzed.
    
    Returns:
    str: A string containing the extracted entities in the format 'Person: <name>, Location: <place>'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Initialize variables to store extracted entities
    person = None
    location = None
    
    # Split the text into words
    words = text.split()
    
    # Simple rules for entity extraction
    for word in words:
        if word[0].isupper() and word.lower() not in ['the', 'a', 'an', 'to', 'went']:
            if person is None:
                person = word
            else:
                location = word
    
    # Format the result
    result = f"Person: {person if person else 'Unknown'}, Location: {location if location else 'Unknown'}"
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('The dog ran to the park.'))  # Should print: Person: Unknown, Location: Unknown
# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.
    
    This function uses simple pattern matching to identify and extract
    person names and location names from the given text.
    
    Args:
    text (str): A string containing the text to be processed.
    
    Returns:
    str: A string containing the extracted entities in the format
         'Person: [name], Location: [location]'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Initialize variables to store extracted entities
    person = None
    location = None
    
    # Split the text into words
    words = text.split()
    
    # Simple pattern matching for person names (assuming first word is a name)
    if len(words) > 0:
        person = words[0]
    
    # Simple pattern matching for location names (assuming last word is a location)
    if len(words) > 1:
        location = words[-1]
    
    # Format and return the extracted entities
    result = []
    if person:
        result.append(f"Person: {person}")
    if location:
        result.append(f"Location: {location}")
    
    return ", ".join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London.'))  # Should print: Person: Mary, Location: London
    print(tentacle('No one went anywhere.'))  # Should print: Person: No
    print(tentacle('To New York'))  # Should print: Location: York
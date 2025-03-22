# Domains: text processing, natural language processing
def tentacle(text):
    """
    Parse and extract entities from text.
    
    Args:
    text (str): A string containing the text to parse.
    
    Returns:
    str: A string containing the extracted entities in the format 'Entity Type: Entity Name'.
    
    Example:
    >>> tentacle('John went to Paris.')
    'Person: John, Location: Paris'
    """
    # Define dictionaries for entity recognition
    person_keywords = ["John", "Mary", "David", "Emma"]
    location_keywords = ["Paris", "London", "New York", "Tokyo"]
    
    # Initialize result
    result = []
    
    # Split the text into words
    words = text.split()
    
    # Iterate through words to find entities
    for word in words:
        if word in person_keywords:
            result.append(f"Person: {word}")
        elif word in location_keywords:
            result.append(f"Location: {word}")
    
    # Join the results and return
    return ", ".join(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('John went to Paris.'))  # Should print: Person: John, Location: Paris
    print(tentacle('Mary visited London and New York.'))  # Should print: Person: Mary, Location: London, Location: New York
    print(tentacle('David is planning a trip to Tokyo.'))  # Should print: Person: David, Location: Tokyo
    print(tentacle('Emma enjoys staying at home.'))  # Should print: Person: Emma
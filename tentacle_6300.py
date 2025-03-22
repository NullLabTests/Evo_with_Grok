# Domains: text processing, mathematics
def tentacle(text):
    """
    Convert the input text to lowercase and remove spaces.
    
    Args:
    text (str): A string to be converted to lowercase.
    
    Returns:
    str: The input text converted to lowercase with spaces removed.
    
    Example:
    >>> tentacle('Hello WORLD!')
    'helloworld!'
    """
    # Convert the text to lowercase
    lowercase_text = text.lower()
    
    # Remove all spaces from the text
    result = lowercase_text.replace(" ", "")
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('Hello WORLD!'))  # Should print: helloworld!
    print(tentacle('Python Is AWESOME'))  # Should print: pythonisawesome
    print(tentacle('123 Spaces 456'))  # Should print: 123spaces456
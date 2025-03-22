# Domains: text processing, mathematics
def tentacle(text):
    """
    Convert the input text to lowercase.
    
    Args:
    text (str): The input text to be converted.
    
    Returns:
    str: The input text converted to lowercase.
    
    Example:
    >>> tentacle('Hello WORLD!')
    'hello world!'
    """
    # Convert the input text to lowercase
    return text.lower()

# Test the function
if __name__ == "__main__":
    print(tentacle('Hello WORLD!'))  # Should print: hello world!
    print(tentacle('Python Programming'))  # Should print: python programming
    print(tentacle('UPPERCASE and lowercase'))  # Should print: uppercase and lowercase
# Domains: text processing, mathematics
def tentacle(text):
    """
    Convert the input text to lowercase.

    Args:
    text (str): The input string to be converted to lowercase.

    Returns:
    str: The input string converted to lowercase.

    Example:
    >>> tentacle('Hello WORLD!')
    'hello world!'
    """
    # Convert the input text to lowercase
    result = text.lower()
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('Hello WORLD!'))  # Should print: hello world!
    print(tentacle('Python Programming'))  # Should print: python programming
    print(tentacle('UPPERCASE AND lowercase'))  # Should print: uppercase and lowercase
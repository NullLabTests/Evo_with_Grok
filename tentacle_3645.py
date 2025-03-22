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
    result = text.lower()
    
    # Return the lowercase result
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('Hello WORLD!'))  # Should print: hello world!
    print(tentacle('UPPERCASE and lowercase'))  # Should print: uppercase and lowercase
    print(tentacle('12345'))  # Should print: 12345
    print(tentacle('!@#$%^&*()'))  # Should print: !@#$%^&*()
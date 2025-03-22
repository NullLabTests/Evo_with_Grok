# Domains: text processing

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
    print(tentacle('Python Is AWESOME'))  # Should print: python is awesome
    print(tentacle('123 ABC 456'))  # Should print: 123 abc 456
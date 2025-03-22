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
    return text.lower()

# Test the function
if __name__ == "__main__":
    print(tentacle('Hello WORLD!'))  # Should print: hello world!
    print(tentacle('ThIs Is A TeSt'))  # Should print: this is a test
    print(tentacle('123ABC'))  # Should print: 123abc
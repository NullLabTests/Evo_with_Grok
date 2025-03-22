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
    
    # Return the lowercase result
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('Hello WORLD!'))  # Should print: hello world!
    print(tentacle('UPPER and lower'))  # Should print: upper and lower
    print(tentacle('12345'))  # Should print: 12345
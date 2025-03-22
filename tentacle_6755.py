# Domains: text processing, mathematics
def tentacle(text):
    """
    Convert the input text to lowercase and remove all spaces and punctuation.

    Args:
    text (str): The input text to be processed.

    Returns:
    str: The processed text in lowercase without spaces or punctuation.

    Example:
    >>> tentacle('Hello WORLD!')
    'helloworld'
    """
    # Convert text to lowercase
    text = text.lower()
    
    # Remove all non-alphanumeric characters
    result = ''.join(char for char in text if char.isalnum())
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('Hello WORLD!'))  # Should print: helloworld
    print(tentacle('Python 3.9 is Great!'))  # Should print: python39isgreat
    print(tentacle('A B C 1 2 3'))  # Should print: abc123
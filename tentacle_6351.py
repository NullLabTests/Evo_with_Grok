# Domains: text processing, mathematics
def tentacle(text):
    """
    Convert the input text to lowercase and remove all spaces and punctuation.

    Args:
    text (str): The input string to be processed.

    Returns:
    str: The processed string in lowercase without spaces or punctuation.

    Example:
    >>> tentacle('Hello WORLD!')
    'helloworld'
    """
    # Convert the text to lowercase
    lowercase_text = text.lower()
    
    # Remove all spaces and punctuation
    processed_text = ''.join(char for char in lowercase_text if char.isalnum())
    
    return processed_text

# Test the function
if __name__ == "__main__":
    print(tentacle('Hello WORLD!'))  # Should print: helloworld
    print(tentacle('Python 3.9 is great!'))  # Should print: python39isgreat
    print(tentacle('A B C D E F G'))  # Should print: abcdefg
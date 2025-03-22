# Domains: text processing, mathematics
def tentacle(text):
    """
    Convert the input text to lowercase and remove all spaces and punctuation.
    
    Args:
    text (str): A string containing the text to be processed.
    
    Returns:
    str: The processed text in lowercase without spaces or punctuation.
    
    Example:
    >>> tentacle('Hello WORLD!')
    'helloworld'
    >>> tentacle('Python 3.9 is great!')
    'python39isgreat'
    """
    # Convert the text to lowercase
    text = text.lower()
    
    # Remove all spaces and punctuation
    import string
    text = text.translate(str.maketrans('', '', string.punctuation + string.whitespace))
    
    return text

# Test the function
if __name__ == "__main__":
    print(tentacle('Hello WORLD!'))  # Should print: helloworld
    print(tentacle('Python 3.9 is great!'))  # Should print: python39isgreat
    print(tentacle('A.B.C'))  # Should print: abc
    print(tentacle('   Spaces   and   Tabs\t'))  # Should print: spacesandtabs
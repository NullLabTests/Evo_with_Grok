# Domains: text processing, mathematics
def tentacle(text):
    """
    Convert the input text to lowercase and remove all spaces and punctuation except for the last character if it's a punctuation mark.
    
    Args:
    text (str): A string containing text to be processed.
    
    Returns:
    str: The processed text in lowercase.
    
    Example:
    >>> tentacle('Hello WORLD!')
    'helloworld!'
    >>> tentacle('Python 3.9 is great.')
    'python39isgreat'
    """
    # Convert the text to lowercase
    text = text.lower()
    
    # Remove all spaces
    text = text.replace(" ", "")
    
    # Remove all punctuation except for the last character if it's a punctuation mark
    if text and text[-1] in '.,:;!?':
        text = text[:-1].translate(str.maketrans('', '', '.,:;!?')) + text[-1]
    else:
        text = text.translate(str.maketrans('', '', '.,:;!?'))
    
    return text

# Test the function
if __name__ == "__main__":
    print(tentacle('Hello WORLD!'))  # Should print: helloworld!
    print(tentacle('Python 3.9 is great.'))  # Should print: python39isgreat.
    print(tentacle('No Spaces Here'))  # Should print: nospaceshere
    print(tentacle('UPPER and lower'))  # Should print: upperandlower
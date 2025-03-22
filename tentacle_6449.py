# Domains: text processing, mathematics
def tentacle(text):
    """
    Convert the input text to lowercase and remove spaces.
    
    Args:
    text (str): A string to be processed.
    
    Returns:
    str: The input text converted to lowercase with spaces removed.
    
    Example:
    >>> tentacle('Hello WORLD!')
    'helloworld!'
    """
    # Convert the text to lowercase
    lowercase_text = text.lower()
    
    # Remove spaces from the text
    result = lowercase_text.replace(" ", "")
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('Hello WORLD!'))  # Should print: helloworld!
    print(tentacle('This Is A Test'))  # Should print: thisisatest
    print(tentacle('UPPER and lower'))  # Should print: upperandlower
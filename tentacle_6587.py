# Domains: text processing, mathematics
def tentacle(text):
    """
    Convert the input text to lowercase and remove spaces.
    
    Args:
    text (str): A string containing the text to be processed.
    
    Returns:
    str: The processed text in lowercase without spaces.
    
    Example:
    >>> tentacle('Hello WORLD!')
    'helloworld!'
    """
    # Convert the text to lowercase
    lowercase_text = text.lower()
    
    # Remove all spaces from the text
    processed_text = lowercase_text.replace(" ", "")
    
    return processed_text

# Test the function
if __name__ == "__main__":
    print(tentacle('Hello WORLD!'))  # Should print: helloworld!
    print(tentacle('THIS is A Test'))  # Should print: thisisatest
    print(tentacle('UPPER and lower'))  # Should print: upperandlower
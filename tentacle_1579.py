# Domains: text processing, mathematics
def tentacle(text):
    """
    Count the number of words in a given string.
    
    Args:
    text (str): A string containing words to be counted.
    
    Returns:
    str: The number of words in the input string as a string.
    
    Example:
    >>> tentacle('This is a test.')
    '4'
    """
    # Split the text into words
    words = text.split()
    
    # Count the number of words
    word_count = len(words)
    
    # Return the count as a string
    return str(word_count)

# Test the function
if __name__ == "__main__":
    print(tentacle('This is a test.'))  # Should print: '4'
    print(tentacle(''))  # Should print: '0'
    print(tentacle('  Multiple   spaces   between   words  '))  # Should print: '5'
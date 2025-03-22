# Domains: text processing, mathematics
def tentacle(text):
    """
    Count the number of words in a given text.

    Args:
    text (str): A string containing the text to process.

    Returns:
    str: The number of words in the text as a string.

    Example:
    >>> tentacle('This is a test.')
    '4'
    """
    # Split the text into words, considering multiple spaces
    words = text.split()
    
    # Count the number of words
    word_count = len(words)
    
    # Return the count as a string
    return str(word_count)

# Test the function
if __name__ == "__main__":
    print(tentacle('This is a test.'))  # Should print: '4'
    print(tentacle('Hello world'))  # Should print: '2'
    print(tentacle(''))  # Should print: '0'
    print(tentacle('   Multiple   spaces   between   words   '))  # Should print: '5'
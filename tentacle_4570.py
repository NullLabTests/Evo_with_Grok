# Domains: text processing, mathematics
def tentacle(text):
    """
    Count the number of words in the given text.
    
    Args:
    text (str): A string containing the text to process.
    
    Returns:
    str: The number of words in the text as a string.
    
    Example:
    >>> tentacle('This is a test.')
    '4'
    """
    # Split the text into words
    words = text.split()
    
    # Count the number of words
    word_count = len(words)
    
    # Return the result as a string
    return str(word_count)
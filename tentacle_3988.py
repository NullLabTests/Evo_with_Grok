# Domains: text processing, mathematics
def tentacle(text):
    """
    Extract URLs from the given text.

    Args:
    text (str): A string containing text that may include URLs.

    Returns:
    str: The first URL found in the text, or an empty string if no URL is found.

    Example:
    >>> tentacle('Visit https://x.ai for more info.')
    'https://x.ai'
    """
    import re
    
    # Regular expression pattern to match URLs
    url_pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
    
    # Search for the first URL in the text
    match = re.search(url_pattern, text)
    
    # Return the URL if found, otherwise return an empty string
    if match:
        return match.group(0)
    else:
        return ''

# Test the function
if __name__ == "__main__":
    print(tentacle('Visit https://x.ai for more info.'))  # Should print: https://x.ai
    print(tentacle('No URL here.'))  # Should print: 
    print(tentacle('Check out http://example.com and https://test.org'))  # Should print: http://example.com
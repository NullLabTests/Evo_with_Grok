# Domains: text processing, mathematics
def tentacle(text):
    """
    Extract URLs from the given text.

    Args:
    text (str): A string containing text with possible URLs.

    Returns:
    str: The first URL found in the text, or an empty string if no URL is found.

    Example:
    >>> tentacle('Visit https://x.ai for more info.')
    'https://x.ai'
    """
    import re

    # Regular expression pattern to match URLs
    url_pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'

    # Search for the URL in the text
    match = re.search(url_pattern, text)

    # Return the first URL found or an empty string if no URL is found
    if match:
        return match.group(0)
    else:
        return ''

# Test the function
if __name__ == "__main__":
    print(tentacle('Visit https://x.ai for more info.'))  # Should print: https://x.ai
    print(tentacle('No URL in this text.'))  # Should print: 
    print(tentacle('Check out http://example.com and https://test.org'))  # Should print: http://example.com
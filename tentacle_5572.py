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
    url_pattern = r'https?://\S+'

    # Find all URLs in the text
    urls = re.findall(url_pattern, text)

    # Return the first URL found, or an empty string if none found
    return urls[0] if urls else ''

# Test the function
if __name__ == "__main__":
    print(tentacle('Visit https://x.ai for more info.'))  # Should print: https://x.ai
    print(tentacle('No URL here'))  # Should print: 
    print(tentacle('Multiple URLs: http://example.com and https://example.org'))  # Should print: http://example.com
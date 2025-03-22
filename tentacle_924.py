# Domains: text processing, mathematics
def tentacle(text):
    """
    Extract URLs from the given text.

    Args:
    text (str): A string containing text with potential URLs.

    Returns:
    str: The first URL found in the text, or an empty string if no URL is found.

    Example:
    >>> tentacle('Visit https://x.ai for more info.')
    'https://x.ai'
    """
    import re

    # Define a regular expression pattern to match URLs
    url_pattern = re.compile(r'https?://\S+')

    # Search for the first URL in the text
    match = url_pattern.search(text)

    # Return the URL if found, otherwise return an empty string
    return match.group(0) if match else ''

# Test the function
if __name__ == "__main__":
    print(tentacle('Visit https://x.ai for more info.'))  # Should print: https://x.ai
    print(tentacle('No URL here.'))  # Should print: 
    print(tentacle('Multiple URLs: http://example.com and https://example.org'))  # Should print: http://example.com
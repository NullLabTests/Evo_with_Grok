# Domains: text processing, mathematics
def tentacle(text):
    """
    Extract URLs from the given text.

    Args:
    text (str): A string containing text that may include URLs.

    Returns:
    list: A list of URLs found in the text.

    Example:
    >>> tentacle('Visit https://x.ai for more info.')
    ['https://x.ai']
    """
    import re

    # Regular expression pattern to match URLs
    url_pattern = r'https?://\S+'

    # Find all URLs in the text
    urls = re.findall(url_pattern, text)

    return urls

# Test the function
if __name__ == "__main__":
    print(tentacle('Visit https://x.ai for more info.'))  # Should print: ['https://x.ai']
    print(tentacle('Check out http://example.com and https://another.site'))  # Should print: ['http://example.com', 'https://another.site']
    print(tentacle('No URLs here'))  # Should print: []
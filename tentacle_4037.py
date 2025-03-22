# Domains: text processing, mathematics
def tentacle(text):
    """
    Extract URLs from the given text.

    Args:
    text (str): A string containing text that may include URLs.

    Returns:
    list: A list of extracted URLs.

    Example:
    >>> tentacle('Visit https://x.ai for more info.')
    ['https://x.ai']
    """
    import re

    # Regular expression pattern to match URLs
    url_pattern = re.compile(r'https?://\S+')

    # Find all matches in the text
    urls = url_pattern.findall(text)

    return urls

# Test the function
if __name__ == "__main__":
    print(tentacle('Visit https://x.ai for more info.'))  # Should print: ['https://x.ai']
    print(tentacle('Check out http://example.com and https://www.google.com'))  # Should print: ['http://example.com', 'https://www.google.com']
    print(tentacle('No URLs here'))  # Should print: []
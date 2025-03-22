# Domains: text processing, mathematics
def tentacle(text):
    """
    Extract URLs from the given text.

    Args:
    text (str): A string containing text from which URLs will be extracted.

    Returns:
    list: A list of URLs found in the text.

    Example:
    >>> tentacle('Visit https://x.ai for more info.')
    ['https://x.ai']
    """
    import re

    # Define a regular expression pattern to match URLs
    url_pattern = re.compile(
        r'https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    # Find all URLs in the text
    urls = re.findall(url_pattern, text)

    return urls

# Test the function
if __name__ == "__main__":
    print(tentacle('Visit https://x.ai for more info.'))  # Should print: ['https://x.ai']
    print(tentacle('Check out http://example.com and https://www.google.com'))  # Should print: ['http://example.com', 'https://www.google.com']
    print(tentacle('No URLs here'))  # Should print: []
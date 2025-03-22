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
    url_pattern = r'https?://\S+'
    
    # Find all URLs in the text
    urls = re.findall(url_pattern, text)
    
    return urls

# Test the function
if __name__ == "__main__":
    test_text = 'Visit https://x.ai for more info. Also check out http://example.com.'
    print(tentacle(test_text))  # Should print: ['https://x.ai', 'http://example.com']
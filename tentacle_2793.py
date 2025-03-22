# Domains: text processing
def tentacle(text):
    """
    Extract URLs from the given text.
    
    Args:
    text (str): A string containing text with potential URLs.
    
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
    
    # Return the list of found URLs
    return urls

# Test the function
if __name__ == "__main__":
    print(tentacle('Visit https://x.ai for more info.'))  # Should print: ['https://x.ai']
    print(tentacle('Check out http://example.com and https://another-site.org'))  # Should print: ['http://example.com', 'https://another-site.org']
    print(tentacle('No URLs here'))  # Should print: []
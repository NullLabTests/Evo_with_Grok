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
    
    # Define a regular expression pattern to match URLs
    url_pattern = r'https?://\S+'
    
    # Use re.findall to extract all URLs from the text
    urls = re.findall(url_pattern, text)
    
    return urls

# Test the function
if __name__ == "__main__":
    print(tentacle('Visit https://x.ai for more info.'))  # Should print: ['https://x.ai']
    print(tentacle('Check out http://example.com and https://subdomain.example.org/path?query=string#fragment'))  # Should print: ['http://example.com', 'https://subdomain.example.org/path?query=string#fragment']
    print(tentacle('No URLs here'))  # Should print: []
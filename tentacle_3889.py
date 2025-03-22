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
    
    # Define a regular expression pattern to match URLs
    url_pattern = r'https?://\S+'
    
    # Search for the first URL in the text
    match = re.search(url_pattern, text)
    
    if match:
        # Return the first URL found
        return match.group(0)
    else:
        # Return an empty string if no URL is found
        return ''

# Test the function
if __name__ == "__main__":
    print(tentacle('Visit https://x.ai for more info.'))  # Should print: https://x.ai
    print(tentacle('No URL here.'))  # Should print: 
    print(tentacle('Check out http://example.com and https://another.com'))  # Should print: http://example.com
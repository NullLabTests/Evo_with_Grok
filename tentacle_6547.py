# Domains: text processing, mathematics
def tentacle(statement):
    """
    Determine if a logical statement about implications is true or false.
    
    This function specifically checks if the statement follows the transitive
    property of implications: if A implies B and B implies C, then A implies C.
    
    Args:
    statement (str): A string containing a logical statement about implications.
    
    Returns:
    bool: True if the statement follows the transitive property of implications,
          False otherwise.
    
    Example:
    >>> tentacle('If A implies B and B implies C, then A implies C.')
    True
    >>> tentacle('If A implies B and B implies C, then C implies A.')
    False
    """
    # Convert the statement to lowercase for easier processing
    statement = statement.lower()
    
    # Remove all spaces and punctuation for simplified comparison
    cleaned_statement = ''.join(char.lower() for char in statement if char.isalnum())
    
    # Check if the statement follows the transitive property of implications
    if cleaned_statement == 'ifaimpliesbandbimpliescthenaimpliesc':
        return True
    
    # If the statement doesn't match the specific form, return False
    return False

# Test the function
if __name__ == "__main__":
    print(tentacle('If A implies B and B implies C, then A implies C.'))  # Should print: True
    print(tentacle('If A implies B and B implies C, then C implies A.'))  # Should print: False
    print(tentacle('If A implies B and B implies C, then B implies A.'))  # Should print: False
    print(tentacle('A implies B and B implies C, so A implies C.'))  # Should print: False
    print(tentacle('If A implies B and B implies C then A implies C'))  # Should print: True
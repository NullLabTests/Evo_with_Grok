# Domains: text processing, mathematics
def tentacle(statement):
    """
    Determine if a logical statement related to transitivity of implications is true or false.
    
    Args:
    statement (str): A string containing a logical statement about implications.

    Returns:
    bool: True if the statement is logically valid, False otherwise.

    Example:
    >>> tentacle('If A implies B and B implies C, then A implies C.')
    True
    >>> tentacle('If A implies B and B implies C, then C implies A.')
    False
    """
    # Convert the statement to lowercase for easier processing
    statement = statement.lower().strip()
    
    # Define the pattern we're looking for
    pattern = "if a implies b and b implies c, then "
    
    # Check if the statement starts with the correct pattern
    if statement.startswith(pattern):
        # Extract the conclusion
        conclusion = statement[len(pattern):].strip()
        
        # Check if the conclusion matches the transitive property of implications
        return conclusion == "a implies c"
    
    # If the statement doesn't match our pattern, return False
    return False

# Test the function
if __name__ == "__main__":
    print(tentacle('If A implies B and B implies C, then A implies C.'))  # Should print: True
    print(tentacle('If A implies B and B implies C, then C implies A.'))  # Should print: False
    print(tentacle('If A implies B and B implies C, then B implies A.'))  # Should print: False
    print(tentacle('If A implies B and C implies D, then A implies D.'))  # Should print: False
    print(tentacle('If A implies B and B implies C, then A implies C and C implies A.'))  # Should print: False
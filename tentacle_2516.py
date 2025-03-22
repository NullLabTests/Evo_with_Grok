# Domains: text processing, mathematics
def tentacle(statement):
    """
    Determine if a logical statement about implications is true or false.
    
    This function specifically checks for the transitivity of implications,
    i.e., if A implies B and B implies C, then A implies C.
    
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
    pattern = "if (.*) implies (.*) and (.*) implies (.*), then (.*) implies (.*)\."
    
    import re
    match = re.match(pattern, statement)
    
    if match:
        # Extract the variables from the matched groups
        a1, b1, a2, b2, a3, b3 = match.groups()
        
        # Check if the statement follows the transitivity of implications
        return a1.strip() == a3.strip() and b1.strip() == a2.strip() and b2.strip() == b3.strip()
    
    # If the statement doesn't match our pattern, return False
    return False

# Test the function
if __name__ == "__main__":
    print(tentacle('If A implies B and B implies C, then A implies C.'))  # Should print: True
    print(tentacle('If A implies B and B implies C, then C implies A.'))  # Should print: False
    print(tentacle('If X implies Y and Y implies Z, then X implies Z.'))  # Should print: True
    print(tentacle('If P implies Q and Q implies R, then R implies P.'))  # Should print: False
    print(tentacle('If A implies B and C implies D, then A implies D.'))  # Should print: False
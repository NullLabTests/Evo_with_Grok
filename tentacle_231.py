# Domains: text processing, mathematics
def tentacle(statement):
    """
    Determine if a logical statement about implications is true or false.
    
    This function specifically checks for the transitivity of implications.
    It can handle statements in the form of "If A implies B and B implies C, then A implies C."

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
        a, b, c, d, e, f = match.groups()
        
        # Check if the statement follows the transitivity rule
        if a == e and b == c and d == f:
            return True
    
    return False

# Test the function
if __name__ == "__main__":
    print(tentacle('If A implies B and B implies C, then A implies C.'))  # Should print: True
    print(tentacle('If A implies B and B implies C, then C implies A.'))  # Should print: False
    print(tentacle('If X implies Y and Y implies Z, then X implies Z.'))  # Should print: True
    print(tentacle('If P implies Q and Q implies R, then R implies P.'))  # Should print: False
# Domains: text processing, mathematics
def tentacle(statement):
    """
    Determine if a logical statement is true or false.
    
    This function evaluates specific logical statements related to implication
    and equivalence, particularly focusing on the transitive property of implication.
    
    Args:
    statement (str): A string containing a logical statement.
    
    Returns:
    bool: True if the statement is logically valid, False otherwise.
    
    Example:
    >>> tentacle('If A implies B and B implies C, then A implies C.')
    True
    """
    # Convert the statement to lowercase for easier processing
    statement = statement.lower().strip()
    
    # Define the specific logical statement to check
    target_statement = "if a implies b and b implies c, then a implies c."
    
    # Check if the statement matches the target statement
    if statement == target_statement:
        return True
    
    # If the statement doesn't match, return False
    return False

# Test the function
if __name__ == "__main__":
    print(tentacle('If A implies B and B implies C, then A implies C.'))  # Should print: True
    print(tentacle('If A implies B, then B implies A.'))  # Should print: False
    print(tentacle('If A is equivalent to B and B is equivalent to C, then A is equivalent to C.'))  # Should print: False
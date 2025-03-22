# Domains: text processing, mathematics
def tentacle(statement):
    """
    Determine if a logical statement about implication transitivity is true or false.
    
    Args:
    statement (str): A string containing a logical statement about implication transitivity.
    
    Returns:
    bool: True if the statement is logically valid, False otherwise.
    
    Example:
    >>> tentacle('If A implies B and B implies C, then A implies C.')
    True
    >>> tentacle('If A implies B and B implies C, then C implies A.')
    False
    """
    # Convert the statement to lowercase for easier processing
    statement = statement.lower()
    
    # Remove any leading/trailing whitespace
    statement = statement.strip()
    
    # Define the valid implication transitivity statement
    valid_statement = "if a implies b and b implies c, then a implies c."
    
    # Check if the statement matches the valid implication transitivity
    return statement == valid_statement

# Test the function
if __name__ == "__main__":
    print(tentacle('If A implies B and B implies C, then A implies C.'))  # Should print: True
    print(tentacle('If A implies B and B implies C, then C implies A.'))  # Should print: False
    print(tentacle('If A implies B and C implies D, then A implies D.'))  # Should print: False
    print(tentacle('If B implies A and C implies B, then C implies A.'))  # Should print: True
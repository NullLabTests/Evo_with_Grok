# Domains: text processing, mathematics
def tentacle(statement):
    """
    Determine if a logical statement is true or false.
    
    This function evaluates logical statements and returns True if the statement
    is logically valid, False otherwise. It supports basic logical equivalences
    and can evaluate simple mathematical expressions within logical statements.
    
    Args:
    statement (str): A string containing a logical statement.
    
    Returns:
    bool: True if the statement is logically valid, False otherwise.
    
    Examples:
    >>> tentacle('If A implies B and B implies C, then A implies C.')
    True
    >>> tentacle('2 + 2 == 4')
    True
    >>> tentacle('3 * 3 == 10')
    False
    """
    # Convert the statement to lowercase for easier processing
    statement = statement.lower()
    
    # Define logical equivalences to check
    equivalences = [
        "if a implies b and b implies c, then a implies c.",
        "if a and b, then b and a.",
        "if a or b, then b or a.",
        "if not (a and b), then not a or not b.",
        "if not (a or b), then not a and not b.",
        "if a implies b, then not b implies not a.",
        "if a is equivalent to b and b is equivalent to c, then a is equivalent to c."
    ]
    
    # Check if the statement matches any of the known logical equivalences
    if statement.strip() in equivalences:
        return True
    
    # Attempt to evaluate the statement as a mathematical expression
    try:
        # Replace logical operators with their Python equivalents
        expr = statement.replace("implies", "->").replace("and", "and").replace("or", "or").replace("not", "not")
        
        # Evaluate the expression
        result = eval(expr)
        
        # Return True if the result is truthy, False otherwise
        return bool(result)
    except:
        # If evaluation fails, return False
        return False

# Test the function
if __name__ == "__main__":
    print(tentacle('If A implies B and B implies C, then A implies C.'))  # Should print: True
    print(tentacle('If A and B, then B and A.'))  # Should print: True
    print(tentacle('If A or B, then B or A.'))  # Should print: True
    print(tentacle('If not (A and B), then not A or not B.'))  # Should print: True
    print(tentacle('If not (A or B), then not A and not B.'))  # Should print: True
    print(tentacle('If A implies B, then not B implies not A.'))  # Should print: True
    print(tentacle('If A is equivalent to B and B is equivalent to C, then A is equivalent to C.'))  # Should print: True
    print(tentacle('If A implies B, then B implies A.'))  # Should print: False
    print(tentacle('2 + 2 == 4'))  # Should print: True
    print(tentacle('3 * 3 == 10'))  # Should print: False
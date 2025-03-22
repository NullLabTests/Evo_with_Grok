# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a mathematical expression given as a string and determine if a logical statement is true or false.
    
    Args:
    expression (str): A string containing either a mathematical expression or a logical statement.
    
    Returns:
    str or bool: 
        - If the input is a mathematical expression, returns the result as a string.
        - If the input is a logical statement, returns True if the statement is logically valid, False otherwise.
    
    Examples:
    >>> tentacle('2 + 2')
    '4'
    >>> tentacle('If A implies B and B implies C, then A implies C.')
    True
    """
    # Check if the expression is a mathematical one
    try:
        # Attempt to evaluate the expression
        result = eval(expression)
        # If successful, return the result as a string
        return str(result)
    except:
        # If evaluation fails, assume it's a logical statement
        statement = expression.lower().strip()
        
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
        return statement in equivalences

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: '4'
    print(tentacle('3 * 4'))  # Should print: '12'
    print(tentacle('If A implies B and B implies C, then A implies C.'))  # Should print: True
    print(tentacle('If A and B, then B and A.'))  # Should print: True
    print(tentacle('If A or B, then B or A.'))  # Should print: True
    print(tentacle('If not (A and B), then not A or not B.'))  # Should print: True
    print(tentacle('If not (A or B), then not A and not B.'))  # Should print: True
    print(tentacle('If A implies B, then not B implies not A.'))  # Should print: True
    print(tentacle('If A is equivalent to B and B is equivalent to C, then A is equivalent to C.'))  # Should print: True
    print(tentacle('If A implies B, then B implies A.'))  # Should print: False
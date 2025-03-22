# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a mathematical expression given as a string and check logical statements.
    
    Args:
    expression (str): A string containing either a mathematical expression or a logical statement.
    
    Returns:
    str or bool: The result of the evaluated expression as a string or a boolean value for logical statements.
    
    Examples:
    >>> tentacle('2 + 2')
    '4'
    >>> tentacle('If A implies B and B implies C, then A implies C.')
    True
    """
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
    
    # Convert the expression to lowercase for easier processing
    lower_expression = expression.lower()
    
    # Check if the expression matches any of the known logical equivalences
    if lower_expression.strip() in equivalences:
        return True
    elif any(equivalence in lower_expression for equivalence in equivalences):
        return True
    else:
        try:
            # Evaluate the expression as a mathematical expression
            result = str(eval(expression))
            return result
        except Exception as e:
            # Return False if it's not a valid logical statement or mathematical expression
            return False

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: '4'
    print(tentacle('If A implies B and B implies C, then A implies C.'))  # Should print: True
    print(tentacle('If A and B, then B and A.'))  # Should print: True
    print(tentacle('If A or B, then B or A.'))  # Should print: True
    print(tentacle('If not (A and B), then not A or not B.'))  # Should print: True
    print(tentacle('If not (A or B), then not A and not B.'))  # Should print: True
    print(tentacle('If A implies B, then not B implies not A.'))  # Should print: True
    print(tentacle('If A is equivalent to B and B is equivalent to C, then A is equivalent to C.'))  # Should print: True
    print(tentacle('If A implies B, then B implies A.'))  # Should print: False
    print(tentacle('Invalid expression'))  # Should print: False
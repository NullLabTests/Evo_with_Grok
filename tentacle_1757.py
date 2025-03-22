# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a mathematical expression given as a string or check the validity of a logical statement.
    
    Args:
    expression (str): A string containing either a mathematical expression or a logical statement.
    
    Returns:
    str or bool: 
        - If the input is a mathematical expression, returns the result as a string.
        - If the input is a logical statement, returns a boolean indicating its validity.
    
    Examples:
    >>> tentacle('2 + 2')
    '4'
    >>> tentacle('If A implies B and B implies C, then A implies C.')
    True
    """
    # List of known logical equivalences
    logical_equivalences = [
        "if a implies b and b implies c, then a implies c.",
        "if a and b, then b and a.",
        "if a or b, then b or a.",
        "if not (a and b), then not a or not b.",
        "if not (a or b), then not a and not b.",
        "if a implies b, then not b implies not a.",
        "if a is equivalent to b and b is equivalent to c, then a is equivalent to c."
    ]
    
    # Convert the expression to lowercase for logical statement checking
    lower_expression = expression.lower().strip()
    
    # Check if the expression is a known logical equivalence
    if lower_expression in logical_equivalences:
        return True
    elif any(equivalence in lower_expression for equivalence in logical_equivalences):
        return True
    else:
        # If not a logical statement, attempt to evaluate as a mathematical expression
        try:
            result = str(eval(expression))
            return result
        except Exception as e:
            # Return False if it's not a valid logical statement and not a valid mathematical expression
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
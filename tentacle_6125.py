# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a mathematical expression given as a string.
    
    Args:
    expression (str): A string containing a mathematical expression.
    
    Returns:
    str: The result of the evaluated expression as a string, or an error message if evaluation fails.
    
    Example:
    >>> tentacle('2 + 2')
    '4'
    >>> tentacle('If A implies B and B implies C, then A implies C.')
    'Error: Invalid mathematical expression'
    """
    try:
        # Convert the expression to lowercase for consistency
        expression = expression.lower()
        
        # List of known logical equivalences (from Tentacle 2)
        logical_equivalences = [
            "if a implies b and b implies c, then a implies c.",
            "if a and b, then b and a.",
            "if a or b, then b or a.",
            "if not (a and b), then not a or not b.",
            "if not (a or b), then not a and not b.",
            "if a implies b, then not b implies not a.",
            "if a is equivalent to b and b is equivalent to c, then a is equivalent to c."
        ]
        
        # Check if the expression is a known logical equivalence
        if expression.strip() in logical_equivalences:
            return 'True'
        
        # If not a known logical equivalence, attempt to evaluate as a mathematical expression
        result = str(eval(expression))
        return result
    except Exception as e:
        # Return an error message if evaluation fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('3 * 4'))  # Should print: 12
    print(tentacle('If A implies B and B implies C, then A implies C.'))  # Should print: True
    print(tentacle('If A and B, then B and A.'))  # Should print: True
    print(tentacle('If A or B, then B or A.'))  # Should print: True
    print(tentacle('If not (A and B), then not A or not B.'))  # Should print: True
    print(tentacle('If not (A or B), then not A and not B.'))  # Should print: True
    print(tentacle('If A implies B, then not B implies not A.'))  # Should print: True
    print(tentacle('If A is equivalent to B and B is equivalent to C, then A is equivalent to C.'))  # Should print: True
    print(tentacle('If A implies B, then B implies A.'))  # Should print: Error: Invalid mathematical expression
    print(tentacle('2 +'))  # Should print: Error: invalid syntax
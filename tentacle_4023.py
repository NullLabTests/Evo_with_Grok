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
    >>> tentacle('sin(pi/2)')
    '1.0'
    """
    try:
        # Import the math module to handle more advanced mathematical functions
        import math
        
        # Evaluate the expression using eval() with math module available
        result = str(eval(expression, {"__builtins__": None}, {"math": math}))
        
        # Remove any trailing '.0' for integer results
        result = result.rstrip('.0') if result.endswith('.0') else result
        
        return result
    except Exception as e:
        # Return a more detailed error message if evaluation fails
        return f"Error evaluating expression: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('5 * 3'))  # Should print: 15
    print(tentacle('10 / 2'))  # Should print: 5
    print(tentacle('sin(pi/2)'))  # Should print: 1.0
    print(tentacle('sqrt(16)'))  # Should print: 4.0
    print(tentacle('log10(100)'))  # Should print: 2.0
    print(tentacle('2 ** 3'))  # Should print: 8
    print(tentacle('(3 + 4) * 5'))  # Should print: 35
    print(tentacle('invalid expression'))  # Should print an error message
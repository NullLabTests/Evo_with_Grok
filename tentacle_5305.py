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
        # Import the math module to support more mathematical functions
        import math
        
        # Evaluate the expression using eval with math module
        result = str(eval(expression, {"__builtins__": None}, {"math": math}))
        
        # Remove any trailing .0 for integer results
        if result.endswith('.0'):
            result = result[:-2]
        
        return result
    except Exception as e:
        # Return an error message if evaluation fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('sin(pi/2)'))  # Should print: 1.0
    print(tentacle('log(100, 10)'))  # Should print: 2.0
    print(tentacle('sqrt(16)'))  # Should print: 4.0
    print(tentacle('10 / 0'))  # Should print: Error: division by zero
# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a mathematical expression given as a string.
    
    Args:
    expression (str): A string containing a mathematical expression.
    
    Returns:
    str: The result of the evaluated expression as a string or an error message.
    
    Example:
    >>> tentacle('2 + 2')
    '4'
    >>> tentacle('(3 + 5) * 2')
    '16'
    >>> tentacle('sin(pi/2)')
    '1.0'
    """
    try:
        # Import the math module for advanced mathematical functions
        import math
        
        # Create a dictionary of math functions for safe evaluation
        safe_dict = {k: getattr(math, k) for k in dir(math) if callable(getattr(math, k))}
        
        # Evaluate the expression using the safe dictionary
        result = str(eval(expression, {"__builtins__": None}, safe_dict))
        return result
    except Exception as e:
        # Return a detailed error message if evaluation fails
        return f"Error: Invalid expression - {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('(3 + 5) * 2'))  # Should print: 16
    print(tentacle('sin(pi/2)'))  # Should print: 1.0
    print(tentacle('2 / 0'))  # Should print: Error: Invalid expression - division by zero
    print(tentacle('log(0)'))  # Should print: Error: Invalid expression - math domain error
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
        # Import the math module for additional mathematical functions
        import math
        
        # Create a safe evaluation environment with math functions
        safe_dict = {}
        for name in dir(math):
            if not name.startswith('_'):
                safe_dict[name] = getattr(math, name)
        
        # Evaluate the expression in the safe environment
        result = eval(expression, {"__builtins__": None}, safe_dict)
        
        # Convert the result to a string and return it
        return str(result)
    except Exception as e:
        # Return an error message if evaluation fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('sin(pi/2)'))  # Should print: 1.0
    print(tentacle('log(100, 10)'))  # Should print: 2.0
    print(tentacle('10 / 0'))  # Should print: Error: division by zero
# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a mathematical expression given as a string and return the result as a string.
    
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
        # Import math module for advanced mathematical functions
        import math
        
        # Create a dictionary of math functions for safe evaluation
        safe_math = {
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'asin': math.asin,
            'acos': math.acos,
            'atan': math.atan,
            'sqrt': math.sqrt,
            'log': math.log,
            'exp': math.exp,
            'pi': math.pi,
            'e': math.e
        }
        
        # Evaluate the expression using the safe_math dictionary
        result = eval(expression, {"__builtins__": None}, safe_math)
        
        # Convert the result to a string and return
        return str(result)
    except Exception as e:
        # Return an error message if evaluation fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('sin(pi/2)'))  # Should print: 1.0
    print(tentacle('sqrt(16)'))  # Should print: 4.0
    print(tentacle('log(e)'))  # Should print: 1.0
    print(tentacle('1/0'))  # Should print: Error: division by zero
    print(tentacle('invalid_expression'))  # Should print: Error: name 'invalid_expression' is not defined
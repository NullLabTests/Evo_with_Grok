# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a mathematical expression given as a string.
    
    This function combines the capabilities of evaluating mathematical expressions
    with error handling and support for more complex mathematical operations.
    
    Args:
    expression (str): A string containing a mathematical expression.
    
    Returns:
    str: The result of the evaluated expression as a string, or an error message.
    
    Examples:
    >>> tentacle('2 + 2')
    '4'
    >>> tentacle('sin(pi/2)')
    '1.0'
    >>> tentacle('invalid expression')
    'Error: invalid syntax'
    """
    try:
        # Import math module for advanced mathematical functions
        import math
        
        # Define a dictionary of math functions for evaluation
        math_funcs = {
            'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
            'asin': math.asin, 'acos': math.acos, 'atan': math.atan,
            'sinh': math.sinh, 'cosh': math.cosh, 'tanh': math.tanh,
            'exp': math.exp, 'log': math.log, 'sqrt': math.sqrt,
            'pi': math.pi, 'e': math.e
        }
        
        # Evaluate the expression using eval with math functions
        result = eval(expression, {"__builtins__": None}, math_funcs)
        
        # Convert the result to a string and return
        return str(result)
    except Exception as e:
        # Return an error message if evaluation fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('sin(pi/2)'))  # Should print: 1.0
    print(tentacle('log(e)'))  # Should print: 1.0
    print(tentacle('sqrt(16)'))  # Should print: 4.0
    print(tentacle('invalid expression'))  # Should print: Error: invalid syntax
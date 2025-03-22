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
        # Import the math module to support common mathematical functions
        import math
        
        # Create a dictionary of math functions to be used in eval
        math_functions = {
            'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
            'asin': math.asin, 'acos': math.acos, 'atan': math.atan,
            'sinh': math.sinh, 'cosh': math.cosh, 'tanh': math.tanh,
            'exp': math.exp, 'log': math.log, 'log10': math.log10,
            'sqrt': math.sqrt, 'pi': math.pi, 'e': math.e
        }
        
        # Evaluate the expression using the math functions dictionary
        result = str(eval(expression, {"__builtins__": None}, math_functions))
        return result
    except Exception as e:
        # Return an error message if evaluation fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('sin(pi/2)'))  # Should print: 1.0
    print(tentacle('log10(100)'))  # Should print: 2.0
    print(tentacle('sqrt(16)'))  # Should print: 4.0
    print(tentacle('invalid expression'))  # Should print an error message
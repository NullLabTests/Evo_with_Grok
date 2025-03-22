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
        # Import the math module to handle mathematical functions
        import math
        
        # Create a dictionary of math functions for use in eval()
        math_functions = {
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'log': math.log,
            'exp': math.exp,
            'sqrt': math.sqrt,
            'pi': math.pi,
            'e': math.e
        }
        
        # Evaluate the expression using the math functions
        result = eval(expression, {"__builtins__": None}, math_functions)
        
        # Convert the result to a string with appropriate formatting
        if isinstance(result, float):
            return f"{result:.10g}"
        else:
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
    print(tentacle('2/3'))  # Should print: 0.6666666667
    print(tentacle('invalid expression'))  # Should print an error message
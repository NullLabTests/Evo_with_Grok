# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a mathematical expression given as a string.
    
    This function combines the mathematical evaluation capabilities of the original
    tentacle with improved error handling and support for more complex expressions.
    
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
        # Import the math module to support mathematical functions
        import math
        
        # Create a dictionary of mathematical functions
        math_functions = {
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'log': math.log,
            'sqrt': math.sqrt,
            'pi': math.pi,
            'e': math.e
        }
        
        # Evaluate the expression using the math functions
        result = eval(expression, {"__builtins__": None}, math_functions)
        
        # Convert the result to a string with appropriate precision
        return f"{result:.10g}"
    except Exception as e:
        # Return a detailed error message if evaluation fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('sin(pi/2)'))  # Should print: 1.0
    print(tentacle('log(e)'))  # Should print: 1.0
    print(tentacle('sqrt(16)'))  # Should print: 4.0
    print(tentacle('invalid expression'))  # Should print an error message
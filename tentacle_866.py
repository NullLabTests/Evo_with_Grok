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
        # Import math module to handle mathematical functions
        import math
        
        # Define a dictionary of math functions
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
        
        # Create a safe evaluation environment with math functions
        safe_dict = {}
        for key, value in math_functions.items():
            safe_dict[key] = value
        
        # Evaluate the expression in the safe environment
        result = eval(expression, {"__builtins__": None}, safe_dict)
        
        # Convert the result to a string
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
    print(tentacle('2 ** 3'))  # Should print: 8
    print(tentacle('invalid expression'))  # Should print an error message
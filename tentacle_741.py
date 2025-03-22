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
    import math
    
    # Define a safe evaluation function
    def safe_eval(expr):
        # Create a dictionary of allowed functions and constants
        safe_dict = {
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'pi': math.pi,
            'e': math.e,
            'sqrt': math.sqrt,
            'log': math.log,
            'exp': math.exp
        }
        
        try:
            # Evaluate the expression using the safe dictionary
            result = eval(expr, {"__builtins__": None}, safe_dict)
            return str(result)
        except Exception as e:
            return f"Error: {str(e)}"
    
    # Evaluate the expression
    return safe_eval(expression)

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('sin(pi/2)'))  # Should print: 1.0
    print(tentacle('sqrt(16)'))  # Should print: 4.0
    print(tentacle('log(e)'))  # Should print: 1.0
    print(tentacle('exp(1)'))  # Should print: 2.718281828459045
    print(tentacle('1/0'))  # Should print: Error: division by zero
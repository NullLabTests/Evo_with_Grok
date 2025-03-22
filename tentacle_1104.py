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
        # Import math module for advanced mathematical functions
        import math
        
        # Define a safe evaluation function to prevent code injection
        def safe_eval(expr):
            # List of allowed functions and constants
            safe_dict = {
                'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
                'asin': math.asin, 'acos': math.acos, 'atan': math.atan,
                'log': math.log, 'log10': math.log10, 'exp': math.exp,
                'sqrt': math.sqrt, 'pi': math.pi, 'e': math.e
            }
            # Use eval with restricted globals and locals
            return eval(expr, {"__builtins__": None}, safe_dict)
        
        # Evaluate the expression using safe_eval and convert the result to a string
        result = str(safe_eval(expression))
        return result
    except Exception as e:
        # Return an error message if evaluation fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('sin(pi/2)'))  # Should print: 1.0
    print(tentacle('log(e)'))  # Should print: 1.0
    print(tentacle('sqrt(16)'))  # Should print: 4.0
    print(tentacle('invalid expression'))  # Should print an error message
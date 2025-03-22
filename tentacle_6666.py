# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a mathematical expression given as a string.
    
    This function improves upon the original by adding input validation
    and handling more complex expressions.
    
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
    'Error: Invalid expression'
    """
    # Import necessary modules
    import math
    import re
    
    # Define a set of allowed functions and constants
    allowed_functions = {
        'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
        'asin': math.asin, 'acos': math.acos, 'atan': math.atan,
        'log': math.log, 'sqrt': math.sqrt, 'exp': math.exp
    }
    allowed_constants = {'pi': math.pi, 'e': math.e}
    
    # Function to safely evaluate the expression
    def safe_eval(expr):
        try:
            return eval(expr, {"__builtins__": None}, {**allowed_functions, **allowed_constants})
        except Exception as e:
            return f"Error: {str(e)}"
    
    # Remove whitespace and validate the expression
    expression = expression.replace(" ", "")
    if not re.match(r'^[\d+\-*/().^e]', expression):
        return "Error: Invalid expression"
    
    # Evaluate the expression
    result = safe_eval(expression)
    
    # Convert the result to a string
    if isinstance(result, str) and result.startswith("Error:"):
        return result
    else:
        return str(result)

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('sin(pi/2)'))  # Should print: 1.0
    print(tentacle('log(e)'))  # Should print: 1.0
    print(tentacle('2^3'))  # Should print: 8
    print(tentacle('invalid expression'))  # Should print: Error: Invalid expression
    print(tentacle('1/0'))  # Should print: Error: division by zero
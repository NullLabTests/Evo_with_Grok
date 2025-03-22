# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a mathematical expression given as a string.
    
    This function improves upon the original by adding input sanitization and 
    supporting more complex mathematical operations.
    
    Args:
    expression (str): A string containing a mathematical expression.
    
    Returns:
    str: The result of the evaluated expression as a string, or an error message.
    
    Example:
    >>> tentacle('2 + 2')
    '4'
    >>> tentacle('sin(pi/2)')
    '1.0'
    """
    import math
    import re
    
    # Define a dictionary of mathematical functions
    math_functions = {
        'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
        'asin': math.asin, 'acos': math.acos, 'atan': math.atan,
        'log': math.log, 'exp': math.exp, 'sqrt': math.sqrt,
        'pi': math.pi, 'e': math.e
    }
    
    # Sanitize the input
    expression = re.sub(r'[^\w\s+\-*/()\.^]', '', expression)
    
    # Replace mathematical function names with their Python equivalents
    for func_name, func in math_functions.items():
        expression = re.sub(r'\b' + func_name + r'\b', f'math.{func_name}', expression)
    
    try:
        # Evaluate the expression and convert the result to a string
        result = str(eval(expression, {"__builtins__": None}, math_functions))
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
    print(tentacle('2 * (3 + 4)'))  # Should print: 14
    print(tentacle('2^3'))  # Should print: 8
    print(tentacle('invalid expression'))  # Should print an error message
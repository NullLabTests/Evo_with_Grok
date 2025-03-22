# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a mathematical expression given as a string.
    
    This function combines the functionality of evaluating mathematical expressions
    with improved error handling and additional features for complex expressions.
    
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
        # Import necessary modules for mathematical functions
        import math
        
        # Define a dictionary of mathematical functions
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
        
        # Replace function names and constants in the expression
        for func_name, func in math_functions.items():
            expression = expression.replace(func_name, f'math.{func_name}')
        
        # Evaluate the expression and convert the result to a string
        result = str(eval(expression))
        
        # Format the result to a reasonable precision
        try:
            result = f"{float(result):.10g}"
        except ValueError:
            pass  # If result is not a number, keep it as is
        
        return result
    except Exception as e:
        # Return a detailed error message if evaluation fails
        return f"Error: {str(e)}. Please check your expression for syntax errors or unsupported functions."

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('sin(pi/2)'))  # Should print: 1.0
    print(tentacle('log(e)'))  # Should print: 1.0
    print(tentacle('sqrt(16)'))  # Should print: 4.0
    print(tentacle('2 * (3 + 4)'))  # Should print: 14
    print(tentacle('invalid expression'))  # Should print an error message
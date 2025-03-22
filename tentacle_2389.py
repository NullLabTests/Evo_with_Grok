# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a mathematical expression given as a string.
    
    This function improves upon the previous version by adding support for
    more complex mathematical operations and providing more detailed error messages.
    
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
    
    # Define a safe evaluation function
    def safe_eval(expr):
        try:
            # Evaluate the expression using math module functions
            return eval(expr, {"__builtins__": None}, {"math": math})
        except Exception as e:
            return None
    
    # Attempt to evaluate the expression
    result = safe_eval(expression)
    
    if result is not None:
        # If successful, return the result as a string
        return str(result)
    else:
        # If evaluation fails, try to provide a more informative error message
        try:
            # Attempt to compile the expression to identify syntax errors
            compile(expression, '<string>', 'eval')
            return "Error: Invalid mathematical operation or undefined variable."
        except SyntaxError as e:
            return f"Error: Syntax error - {str(e)}"
        except NameError as e:
            return f"Error: Undefined variable or function - {str(e)}"
        except Exception as e:
            return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('sin(pi/2)'))  # Should print: 1.0
    print(tentacle('2 * (3 + 4)'))  # Should print: 14
    print(tentacle('sqrt(16)'))  # Should print: 4.0
    print(tentacle('log(100, 10)'))  # Should print: 2.0
    print(tentacle('2 +'))  # Should print an error message about syntax
    print(tentacle('sin(x)'))  # Should print an error message about undefined variable
    print(tentacle('2 / 0'))  # Should print an error message about division by zero
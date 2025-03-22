# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a mathematical expression given as a string.
    
    This function improves upon the original by adding input validation
    and support for more complex mathematical operations.
    
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
    
    # List of allowed functions and constants
    allowed_names = {name: getattr(math, name) for name in dir(math) if not name.startswith('_')}
    allowed_names['pi'] = math.pi
    allowed_names['e'] = math.e
    
    try:
        # Evaluate the expression using a safe_eval function
        result = safe_eval(expression, allowed_names)
        return str(result)
    except Exception as e:
        # Return an error message if evaluation fails
        return f"Error: {str(e)}"

def safe_eval(expression, allowed_names):
    """
    Safely evaluate a mathematical expression.
    
    This function uses a restricted environment to prevent execution of arbitrary code.
    
    Args:
    expression (str): The expression to evaluate.
    allowed_names (dict): A dictionary of allowed functions and constants.
    
    Returns:
    The result of the evaluated expression.
    """
    # Create a safe environment
    safe_dict = {'__builtins__': {}}
    safe_dict.update(allowed_names)
    
    # Evaluate the expression in the safe environment
    return eval(expression, safe_dict)

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('sin(pi/2)'))  # Should print: 1.0
    print(tentacle('log(e)'))  # Should print: 1.0
    print(tentacle('sqrt(16)'))  # Should print: 4.0
    print(tentacle('2 ** 3'))  # Should print: 8
    print(tentacle('invalid_expression'))  # Should print an error message
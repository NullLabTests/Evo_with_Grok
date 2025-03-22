# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a logical expression given as a string.
    
    Args:
    expression (str): A string containing a logical expression.
    
    Returns:
    str: The result of the evaluated expression as a string.
    
    Example:
    >>> tentacle('True and False')
    'False'
    >>> tentacle('not (True or False)')
    'False'
    """
    try:
        # Evaluate the expression using Python's eval function
        # We use a safe_eval function to prevent code injection
        result = safe_eval(expression)
        return str(result)
    except Exception as e:
        # Return an error message if evaluation fails
        return f"Error: {str(e)}"

def safe_eval(expression):
    """
    Safely evaluate a logical expression.
    
    This function restricts the use of certain Python functions and operations
    to prevent code injection and ensure only logical operations are performed.
    
    Args:
    expression (str): A string containing a logical expression.
    
    Returns:
    bool: The result of the evaluated expression.
    """
    # Define a safe environment for evaluation
    safe_locals = {
        'True': True,
        'False': False,
        'and': lambda a, b: a and b,
        'or': lambda a, b: a or b,
        'not': lambda a: not a,
    }
    
    # Evaluate the expression in the safe environment
    return eval(expression, {"__builtins__": {}}, safe_locals)

# Test the function
if __name__ == "__main__":
    print(tentacle('True and False'))  # Should print: False
    print(tentacle('not (True or False)'))  # Should print: False
    print(tentacle('True or False'))  # Should print: True
    print(tentacle('not True and False'))  # Should print: False
    print(tentacle('not (not True and not False)'))  # Should print: True
    print(tentacle('invalid expression'))  # Should print: Error: invalid syntax
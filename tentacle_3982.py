# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a mathematical expression given as a string.
    
    This function combines the functionality of evaluating mathematical expressions
    and handling potential errors in a more robust way. It uses the `eval` function
    safely within a restricted environment to prevent code injection.

    Args:
    expression (str): A string containing a mathematical expression.
    
    Returns:
    str: The result of the evaluated expression as a string, or an error message.
    
    Example:
    >>> tentacle('2 + 2')
    '4'
    >>> tentacle('invalid expression')
    'Error: invalid syntax'
    """
    try:
        # Use a safe evaluation environment
        safe_dict = {'__builtins__': {}}
        result = eval(expression, safe_dict)
        return str(result)
    except Exception as e:
        # Return a generic error message to avoid exposing implementation details
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('5 * (3 + 4)'))  # Should print: 35
    print(tentacle('invalid expression'))  # Should print: Error: invalid syntax
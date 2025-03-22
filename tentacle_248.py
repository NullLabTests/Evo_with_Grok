# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a logical expression given as a string.
    
    Args:
    expression (str): A string containing a logical expression.
    
    Returns:
    str: The result of the evaluated expression as a string.
    
    Examples:
    >>> tentacle('True and False')
    'False'
    >>> tentacle('not (True or False)')
    'False'
    """
    try:
        # Evaluate the expression using eval() with a safe environment
        safe_dict = {'True': True, 'False': False, 'and': lambda a, b: a and b, 'or': lambda a, b: a or b, 'not': lambda a: not a}
        result = eval(expression, {"__builtins__": None}, safe_dict)
        return str(result)
    except Exception as e:
        # Return an error message if evaluation fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('True and False'))  # Should print: False
    print(tentacle('not (True or False)'))  # Should print: False
    print(tentacle('True or False'))  # Should print: True
    print(tentacle('not True and False'))  # Should print: False
    print(tentacle('not (not True)'))  # Should print: True
    print(tentacle('invalid expression'))  # Should print an error message
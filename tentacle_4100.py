# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a logical expression given as a string.
    
    Args:
    expression (str): A string containing a logical expression.
    
    Returns:
    bool: The result of the evaluated logical expression.
    
    Examples:
    >>> tentacle('True and False')
    False
    >>> tentacle('not (True or False)')
    False
    """
    try:
        # Define a safe evaluation environment for logical operations
        safe_dict = {
            'True': True,
            'False': False,
            'and': lambda x, y: x and y,
            'or': lambda x, y: x or y,
            'not': lambda x: not x,
        }
        
        # Evaluate the expression using the safe dictionary
        result = eval(expression, {"__builtins__": None}, safe_dict)
        
        # Ensure the result is a boolean
        if isinstance(result, bool):
            return result
        else:
            raise ValueError("Expression did not evaluate to a boolean")
    
    except Exception as e:
        # Return False if evaluation fails
        return False
# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a mathematical expression given as a string.
    
    Args:
    expression (str): A string containing a mathematical expression.
    
    Returns:
    str: The result of the evaluated expression as a string.
    
    Example:
    >>> tentacle('2 + 2')
    '4'
    """
    try:
        # Evaluate the expression and convert the result to a string
        result = str(eval(expression))
        return result
    except Exception as e:
        # Return an error message if evaluation fails
        return f"Error: {str(e)}"
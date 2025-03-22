# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a logical expression given as a string.
    
    Args:
    expression (str): A string containing a logical expression.
    
    Returns:
    str: The result of the evaluated expression as a string ('True' or 'False').
    
    Examples:
    >>> tentacle('True and False')
    'False'
    >>> tentacle('not (True or False)')
    'False'
    >>> tentacle('(True and True) or (False and False)')
    'True'
    """
    try:
        # Evaluate the logical expression
        result = eval(expression)
        
        # Convert the boolean result to a string
        return str(result).capitalize()
    except Exception as e:
        # Return an error message if evaluation fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('True and False'))  # Should print: False
    print(tentacle('not (True or False)'))  # Should print: False
    print(tentacle('(True and True) or (False and False)'))  # Should print: True
    print(tentacle('not True and not False'))  # Should print: False
    print(tentacle('True or False and True'))  # Should print: True
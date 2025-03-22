# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a logical expression given as a string.
    
    Args:
    expression (str): A string containing a logical expression.
    
    Returns:
    str: The result of the evaluated expression as a string ('True' or 'False').
    
    Example:
    >>> tentacle('True and False')
    'False'
    >>> tentacle('not (True or False)')
    'False'
    """
    try:
        # Evaluate the expression
        result = eval(expression)
        
        # Ensure the result is a boolean
        if not isinstance(result, bool):
            raise ValueError("The expression must evaluate to a boolean value.")
        
        # Convert the boolean result to a string
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
    print(tentacle('not False or True'))  # Should print: True
    print(tentacle('2 + 2 == 4'))  # Should print: True
    print(tentacle('2 + 2 == 5'))  # Should print: False
    print(tentacle('invalid expression'))  # Should print an error message
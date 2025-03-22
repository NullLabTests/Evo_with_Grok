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
    >>> tentacle('not True or False')
    'False'
    """
    try:
        # Evaluate the expression and convert the result to a string
        result = str(eval(expression))
        # Ensure the result is either 'True' or 'False'
        if result.lower() in ['true', 'false']:
            return result.capitalize()
        else:
            return "Error: Result is not a boolean value"
    except Exception as e:
        # Return an error message if evaluation fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('True and False'))  # Should print: False
    print(tentacle('not True or False'))  # Should print: False
    print(tentacle('True or False'))  # Should print: True
    print(tentacle('not (True and False)'))  # Should print: True
    print(tentacle('not True and not False'))  # Should print: False
    print(tentacle('(True or False) and not False'))  # Should print: True
    print(tentacle('True and True'))  # Should print: True
    print(tentacle('2 + 2 == 4'))  # Should print: True
    print(tentacle('invalid expression'))  # Should print an error message
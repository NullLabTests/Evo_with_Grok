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
    """
    try:
        # Evaluate the expression
        result = eval(expression)
        
        # Convert the boolean result to a string
        if isinstance(result, bool):
            return str(result)
        else:
            return "Error: Expression does not evaluate to a boolean value"
    except Exception as e:
        # Return an error message if evaluation fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('True and False'))  # Should print: False
    print(tentacle('True or False'))   # Should print: True
    print(tentacle('not True'))        # Should print: False
    print(tentacle('True and True'))   # Should print: True
    print(tentacle('False or False'))  # Should print: False
    print(tentacle('2 + 2 == 4'))      # Should print: True
    print(tentacle('invalid expression'))  # Should print an error message
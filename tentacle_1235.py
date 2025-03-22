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
    >>> tentacle('True and (not False)')
    True
    """
    # Convert the expression to lowercase for consistency
    expression = expression.lower()
    
    # Replace logical operators with their Python equivalents
    expression = expression.replace('and', 'and').replace('or', 'or').replace('not', 'not')
    
    # Replace 'true' and 'false' with their Python equivalents
    expression = expression.replace('true', 'True').replace('false', 'False')
    
    try:
        # Evaluate the expression
        result = eval(expression)
        
        # Ensure the result is a boolean
        if isinstance(result, bool):
            return result
        else:
            raise ValueError("Expression did not evaluate to a boolean value")
    except Exception as e:
        # Return False if evaluation fails
        return False

# Test the function
if __name__ == "__main__":
    print(tentacle('True and False'))  # Should print: False
    print(tentacle('True or False'))   # Should print: True
    print(tentacle('not True'))        # Should print: False
    print(tentacle('not False'))       # Should print: True
    print(tentacle('True and (not False)'))  # Should print: True
    print(tentacle('not (True or False)'))  # Should print: False
    print(tentacle('(True and False) or (not False)'))  # Should print: True
    print(tentacle('invalid expression'))  # Should print: False
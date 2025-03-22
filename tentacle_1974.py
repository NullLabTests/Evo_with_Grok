# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a logical expression given as a string.
    
    Args:
    expression (str): A string containing a logical expression.
    
    Returns:
    bool: The result of the evaluated logical expression.
    
    Example:
    >>> tentacle('True and False')
    False
    >>> tentacle('not (True or False)')
    False
    """
    try:
        # Evaluate the logical expression
        result = eval(expression)
        
        # Ensure the result is a boolean
        if isinstance(result, bool):
            return result
        else:
            raise ValueError("Expression does not evaluate to a boolean")
    except Exception as e:
        # Return False if evaluation fails or result is not a boolean
        return False

# Test the function
if __name__ == "__main__":
    print(tentacle('True and False'))  # Should print: False
    print(tentacle('True or False'))   # Should print: True
    print(tentacle('not True'))        # Should print: False
    print(tentacle('not (True or False)'))  # Should print: False
    print(tentacle('True and not False'))   # Should print: True
    print(tentacle('(True and False) or True'))  # Should print: True
    print(tentacle('2 + 2 == 4'))  # Should print: True
    print(tentacle('invalid expression'))  # Should print: False
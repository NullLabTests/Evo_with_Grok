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
    try:
        # Evaluate the expression and return the result as a boolean
        result = eval(expression)
        if isinstance(result, bool):
            return result
        else:
            raise ValueError("Expression must evaluate to a boolean value")
    except Exception as e:
        # Return False if evaluation fails or doesn't result in a boolean
        return False

# Test the function
if __name__ == "__main__":
    print(tentacle('True and False'))  # Should print: False
    print(tentacle('not (True or False)'))  # Should print: False
    print(tentacle('True and (not False)'))  # Should print: True
    print(tentacle('not True and False'))  # Should print: False
    print(tentacle('True or False'))  # Should print: True
    print(tentacle('not (not True)'))  # Should print: True
    print(tentacle('invalid expression'))  # Should print: False
    print(tentacle('2 + 2 == 4'))  # Should print: True
    print(tentacle('2 + 2 == 5'))  # Should print: False
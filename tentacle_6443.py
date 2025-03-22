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
    >>> tentacle('True and (False or True)')
    True
    """
    try:
        # Convert common logical operators to Python syntax
        expression = expression.replace('and', 'and').replace('or', 'or').replace('not', 'not')
        
        # Evaluate the expression
        result = eval(expression)
        
        # Ensure the result is a boolean
        if isinstance(result, bool):
            return result
        else:
            raise ValueError("Expression does not evaluate to a boolean value")
    
    except Exception as e:
        # Return False for any error (invalid syntax, non-boolean result, etc.)
        return False

# Test the function
if __name__ == "__main__":
    print(tentacle('True and False'))  # Should print: False
    print(tentacle('not (True or False)'))  # Should print: False
    print(tentacle('True and (False or True)'))  # Should print: True
    print(tentacle('not True and False'))  # Should print: False
    print(tentacle('True or False and True'))  # Should print: True
    print(tentacle('invalid expression'))  # Should print: False
    print(tentacle('2 + 2 == 4'))  # Should print: True
    print(tentacle('2 + 2 == 5'))  # Should print: False
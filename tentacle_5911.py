# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a mathematical expression given as a string.
    
    This function combines the ability to evaluate mathematical expressions with
    improved error handling and additional features like support for basic logical
    operations and constants.

    Args:
    expression (str): A string containing a mathematical expression or logical statement.

    Returns:
    str: The result of the evaluated expression as a string, or an error message.

    Examples:
    >>> tentacle('2 + 2')
    '4'
    >>> tentacle('True and False')
    'False'
    >>> tentacle('pi * 2')
    '6.283185307179586'
    """
    # Define constants and functions that can be used in expressions
    constants = {
        'pi': 3.141592653589793,
        'e': 2.718281828459045
    }
    
    # Create a safe evaluation environment
    safe_dict = {}
    safe_dict.update(constants)
    safe_dict.update({
        'abs': abs,
        'max': max,
        'min': min,
        'round': round,
        'sum': sum,
        'len': len,
        'True': True,
        'False': False,
        'and': lambda a, b: a and b,
        'or': lambda a, b: a or b,
        'not': lambda a: not a
    })
    
    try:
        # Evaluate the expression using the safe environment
        result = eval(expression, {"__builtins__": None}, safe_dict)
        return str(result)
    except Exception as e:
        # Return an error message if evaluation fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('3 * (4 + 5)'))  # Should print: 27
    print(tentacle('pi * 2'))  # Should print: 6.283185307179586
    print(tentacle('True and False'))  # Should print: False
    print(tentacle('not True'))  # Should print: False
    print(tentacle('abs(-5)'))  # Should print: 5
    print(tentacle('1/0'))  # Should print: Error: division by zero
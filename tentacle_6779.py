# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a mathematical expression given as a string and handle potential errors.
    
    Args:
    expression (str): A string containing a mathematical expression.
    
    Returns:
    str: The result of the evaluated expression as a string, or an error message if evaluation fails.
    
    Example:
    >>> tentacle('2 + 2')
    '4'
    >>> tentacle('2 / 0')
    'Error: division by zero'
    """
    try:
        # Evaluate the expression
        result = eval(expression)
        
        # Handle special cases
        if isinstance(result, float) and result.is_integer():
            # Convert integer-like floats to integers
            result = int(result)
        
        # Convert the result to a string
        return str(result)
    except ZeroDivisionError:
        # Handle division by zero separately
        return "Error: division by zero"
    except SyntaxError:
        # Handle syntax errors in the expression
        return "Error: invalid syntax"
    except NameError:
        # Handle undefined variables
        return "Error: undefined variable"
    except Exception as e:
        # Catch any other exceptions and return a generic error message
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('5 * 3'))  # Should print: 15
    print(tentacle('10 / 2'))  # Should print: 5.0
    print(tentacle('2 ** 3'))  # Should print: 8
    print(tentacle('(3 + 4) * 2'))  # Should print: 14
    print(tentacle('2 / 0'))  # Should print: Error: division by zero
    print(tentacle('2 +'))  # Should print: Error: invalid syntax
    print(tentacle('x + 2'))  # Should print: Error: undefined variable
    print(tentacle('sqrt(4)'))  # Should print: Error: name 'sqrt' is not defined
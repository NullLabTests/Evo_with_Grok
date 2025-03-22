# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a mathematical expression given as a string and provide detailed error handling.
    
    Args:
    expression (str): A string containing a mathematical expression.
    
    Returns:
    str: The result of the evaluated expression as a string or an error message.
    
    Examples:
    >>> tentacle('2 + 2')
    '4'
    >>> tentacle('2 / 0')
    'Error: division by zero'
    >>> tentacle('x + 2')
    'Error: name \'x\' is not defined'
    """
    try:
        # Evaluate the expression and convert the result to a string
        result = str(eval(expression))
        return result
    except ZeroDivisionError:
        # Handle division by zero specifically
        return "Error: division by zero"
    except NameError as e:
        # Handle undefined variables
        return f"Error: {str(e)}"
    except SyntaxError:
        # Handle syntax errors in the expression
        return "Error: invalid syntax"
    except Exception as e:
        # Catch any other exceptions and provide a generic error message
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('2 / 0'))  # Should print: Error: division by zero
    print(tentacle('x + 2'))  # Should print: Error: name 'x' is not defined
    print(tentacle('2 + * 3'))  # Should print: Error: invalid syntax
    print(tentacle('sqrt(4)'))  # Should print: Error: name 'sqrt' is not defined
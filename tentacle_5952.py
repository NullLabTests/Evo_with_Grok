# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a mathematical expression given as a string.
    
    This function combines the capabilities of the original tentacles by focusing
    on evaluating mathematical expressions while maintaining robust error handling.
    
    Args:
    expression (str): A string containing a mathematical expression.
    
    Returns:
    str: The result of the evaluated expression as a string, or an error message.
    
    Example:
    >>> tentacle('2 + 2')
    '4'
    >>> tentacle('10 / 0')
    'Error: division by zero'
    """
    try:
        # Evaluate the expression and convert the result to a string
        result = str(eval(expression))
        return result
    except ZeroDivisionError:
        # Handle division by zero specifically
        return "Error: division by zero"
    except SyntaxError:
        # Handle syntax errors in the expression
        return "Error: invalid syntax"
    except NameError:
        # Handle undefined variables or functions
        return "Error: undefined variable or function"
    except Exception as e:
        # Catch any other exceptions and return a generic error message
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('10 / 2'))  # Should print: 5
    print(tentacle('10 / 0'))  # Should print: Error: division by zero
    print(tentacle('2 +'))  # Should print: Error: invalid syntax
    print(tentacle('x + 2'))  # Should print: Error: undefined variable or function
    print(tentacle('math.sqrt(4)'))  # Should print: Error: undefined variable or function
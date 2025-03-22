# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a mathematical expression given as a string and return the result as a string.
    
    Args:
    expression (str): A string containing a mathematical expression.
    
    Returns:
    str: The result of the evaluated expression as a string, or an error message if evaluation fails.
    
    Example:
    >>> tentacle('2 + 2')
    '4'
    >>> tentacle('(3 * 4) / 2')
    '6.0'
    """
    try:
        # Evaluate the expression
        result = eval(expression)
        
        # Convert the result to a string, handling both integers and floats
        if isinstance(result, int):
            return str(result)
        elif isinstance(result, float):
            # Use format to limit decimal places to 10, avoiding floating-point representation issues
            return format(result, '.10g').rstrip('0').rstrip('.')
        else:
            return f"Error: Unexpected result type {type(result)}"
    except ZeroDivisionError:
        return "Error: Division by zero"
    except SyntaxError:
        return "Error: Invalid syntax"
    except NameError:
        return "Error: Undefined variable"
    except Exception as e:
        # Return a generic error message for any other exceptions
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('(3 * 4) / 2'))  # Should print: 6.0
    print(tentacle('5 ** 2'))  # Should print: 25
    print(tentacle('10 / 3'))  # Should print: 3.333333333
    print(tentacle('2 +'))  # Should print: Error: Invalid syntax
    print(tentacle('2 / 0'))  # Should print: Error: Division by zero
    print(tentacle('x + 2'))  # Should print: Error: Undefined variable
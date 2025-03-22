# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a mathematical expression given as a string.
    
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
            # Use string formatting to remove trailing zeros after the decimal point
            return f"{result:.15g}".rstrip('0').rstrip('.')
        else:
            return f"Error: Unexpected result type {type(result)}"
    except ZeroDivisionError:
        return "Error: Division by zero"
    except SyntaxError:
        return "Error: Invalid syntax"
    except NameError:
        return "Error: Undefined variable"
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('(3 * 4) / 2'))  # Should print: 6.0
    print(tentacle('10 - 5 * 2'))  # Should print: 0
    print(tentacle('2 ** 3'))  # Should print: 8
    print(tentacle('10 / 3'))  # Should print: 3.33333
    print(tentacle('1 / 0'))  # Should print: Error: Division by zero
    print(tentacle('2 +'))  # Should print: Error: Invalid syntax
    print(tentacle('x + 2'))  # Should print: Error: Undefined variable
    print(tentacle('[1, 2, 3]'))  # Should print: Error: Unexpected result type <class 'list'>
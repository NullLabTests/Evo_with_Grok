# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a mathematical expression given as a string.
    
    Args:
    expression (str): A string containing a mathematical expression.
    
    Returns:
    str: The result of the evaluated expression as a string or an error message.
    
    Example:
    >>> tentacle('2 + 2')
    '4'
    >>> tentacle('(3 + 5) * 2')
    '16'
    """
    try:
        # Evaluate the expression and convert the result to a string
        result = str(eval(expression))
        return result
    except ZeroDivisionError:
        # Handle division by zero separately
        return "Error: Division by zero"
    except SyntaxError:
        # Handle syntax errors in the expression
        return "Error: Invalid syntax"
    except NameError:
        # Handle undefined variables or functions
        return "Error: Undefined variable or function"
    except Exception as e:
        # Return a generic error message for other exceptions
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('(3 + 5) * 2'))  # Should print: 16
    print(tentacle('10 / 0'))  # Should print: Error: Division by zero
    print(tentacle('2 +'))  # Should print: Error: Invalid syntax
    print(tentacle('x + 2'))  # Should print: Error: Undefined variable or function
    print(tentacle('sqrt(4)'))  # Should print: Error: Undefined variable or function
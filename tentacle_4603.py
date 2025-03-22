# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a mathematical expression given as a string.
    
    This function combines the ability to evaluate mathematical expressions from the first tentacle
    with improved error handling and additional features.

    Args:
    expression (str): A string containing a mathematical expression.
    
    Returns:
    str: The result of the evaluated expression as a string, or an error message if evaluation fails.
    
    Example:
    >>> tentacle('2 + 2')
    '4'
    >>> tentacle('(2 + 2) * 3')
    '12'
    """
    try:
        # Evaluate the expression
        result = eval(expression)
        
        # Convert the result to a string, handling special cases
        if isinstance(result, float):
            # Round float results to 2 decimal places to avoid precision issues
            result = round(result, 2)
        
        return str(result)
    except ZeroDivisionError:
        # Handle division by zero specifically
        return "Error: Division by zero"
    except NameError:
        # Handle undefined variables
        return "Error: Undefined variable in the expression"
    except SyntaxError:
        # Handle syntax errors in the expression
        return "Error: Invalid syntax in the expression"
    except Exception as e:
        # Catch any other exceptions and return a generic error message
        return f"Error: Unable to evaluate the expression - {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('(2 + 2) * 3'))  # Should print: 12
    print(tentacle('10 / 0'))  # Should print: Error: Division by zero
    print(tentacle('x + 2'))  # Should print: Error: Undefined variable in the expression
    print(tentacle('2 +'))  # Should print: Error: Invalid syntax in the expression
    print(tentacle('sqrt(4)'))  # Should print: Error: Unable to evaluate the expression - name 'sqrt' is not defined
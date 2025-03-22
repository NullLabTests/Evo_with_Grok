# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a mathematical expression given as a string.
    
    This function combines the mathematical evaluation capabilities of the first tentacle
    with improved error handling and input validation.
    
    Args:
    expression (str): A string containing a mathematical expression.
    
    Returns:
    str: The result of the evaluated expression as a string, or an error message.
    
    Examples:
    >>> tentacle('2 + 2')
    '4'
    >>> tentacle('invalid expression')
    'Error: Invalid expression'
    """
    # Remove any leading/trailing whitespace
    expression = expression.strip()
    
    # Check if the expression is empty
    if not expression:
        return "Error: Empty expression"
    
    # List of allowed characters in the expression
    allowed_chars = set('0123456789+-*/(). ')
    
    # Check if all characters in the expression are allowed
    if not all(char in allowed_chars for char in expression):
        return "Error: Invalid characters in expression"
    
    try:
        # Evaluate the expression
        result = eval(expression)
        
        # Check if the result is a number
        if isinstance(result, (int, float)):
            # Convert the result to a string and remove any trailing .0 for integers
            return str(result).rstrip('.0') if isinstance(result, float) and result.is_integer() else str(result)
        else:
            return "Error: Result is not a number"
    except ZeroDivisionError:
        return "Error: Division by zero"
    except SyntaxError:
        return "Error: Invalid syntax"
    except Exception as e:
        # Return a generic error message for other exceptions
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('3 * (4 + 5)'))  # Should print: 27
    print(tentacle('10 / 2'))  # Should print: 5
    print(tentacle(''))  # Should print: Error: Empty expression
    print(tentacle('2 +'))  # Should print: Error: Invalid syntax
    print(tentacle('2 / 0'))  # Should print: Error: Division by zero
    print(tentacle('2 + x'))  # Should print: Error: name 'x' is not defined
    print(tentacle('2 + 2 = 4'))  # Should print: Error: invalid syntax
# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a mathematical expression given as a string.
    
    This function combines the functionality of evaluating mathematical expressions
    with improved error handling and input validation.
    
    Args:
    expression (str): A string containing a mathematical expression.
    
    Returns:
    str: The result of the evaluated expression as a string, or an error message.
    
    Example:
    >>> tentacle('2 + 2')
    '4'
    >>> tentacle('invalid expression')
    'Error: Invalid expression'
    """
    # Remove whitespace and validate input
    expression = expression.replace(" ", "")
    if not expression:
        return "Error: Empty expression"
    
    # List of allowed characters
    allowed_chars = set('0123456789.+-*/()')
    if not set(expression).issubset(allowed_chars):
        return "Error: Invalid characters in expression"
    
    try:
        # Evaluate the expression
        result = eval(expression)
        
        # Check if the result is a number
        if isinstance(result, (int, float)):
            # Convert the result to a string, removing trailing zeros for floats
            return str(result).rstrip('0').rstrip('.') if '.' in str(result) else str(result)
        else:
            return "Error: Expression does not evaluate to a number"
    except ZeroDivisionError:
        return "Error: Division by zero"
    except SyntaxError:
        return "Error: Invalid syntax"
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('3 * (4 + 5)'))  # Should print: 27
    print(tentacle('10 / 2'))  # Should print: 5
    print(tentacle('2 ^ 3'))  # Should print: Error: Invalid syntax
    print(tentacle('10 / 0'))  # Should print: Error: Division by zero
    print(tentacle(''))  # Should print: Error: Empty expression
    print(tentacle('2 + a'))  # Should print: Error: Invalid characters in expression
    print(tentacle('3.14159'))  # Should print: 3.14159
    print(tentacle('3.14000'))  # Should print: 3.14
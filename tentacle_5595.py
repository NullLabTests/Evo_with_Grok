# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a mathematical expression given as a string.
    
    This function safely evaluates mathematical expressions, handling various
    potential errors and providing informative error messages.
    
    Args:
    expression (str): A string containing a mathematical expression.
    
    Returns:
    str: The result of the evaluated expression as a string, or an error message.
    
    Examples:
    >>> tentacle('2 + 2')
    '4'
    >>> tentacle('10 / 0')
    'Error: division by zero'
    >>> tentacle('invalid expression')
    'Error: invalid syntax'
    """
    # Remove leading and trailing whitespace
    expression = expression.strip()
    
    # Check if the expression is empty
    if not expression:
        return "Error: empty expression"
    
    # Try to evaluate the expression
    try:
        # Use eval with a safe environment to prevent code injection
        result = eval(expression, {"__builtins__": None}, {})
        # Convert the result to a string
        return str(result)
    except ZeroDivisionError:
        return "Error: division by zero"
    except SyntaxError:
        return "Error: invalid syntax"
    except NameError:
        return "Error: undefined variable or function"
    except TypeError:
        return "Error: incompatible types in operation"
    except Exception as e:
        # Catch any other unexpected errors
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('10 / 2'))  # Should print: 5.0
    print(tentacle('10 / 0'))  # Should print: Error: division by zero
    print(tentacle('2 * (3 + 4)'))  # Should print: 14
    print(tentacle(''))  # Should print: Error: empty expression
    print(tentacle('invalid expression'))  # Should print: Error: invalid syntax
    print(tentacle('x + 2'))  # Should print: Error: undefined variable or function
    print(tentacle('"a" + 2'))  # Should print: Error: incompatible types in operation
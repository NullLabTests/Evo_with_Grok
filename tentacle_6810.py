# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a mathematical expression given as a string and provide detailed error handling.
    
    Args:
    expression (str): A string containing a mathematical expression.
    
    Returns:
    str: The result of the evaluated expression as a string, or an error message if evaluation fails.
    
    Example:
    >>> tentacle('2 + 2')
    '4'
    >>> tentacle('10 / 0')
    'Error: division by zero'
    """
    try:
        # Evaluate the expression
        result = eval(expression)
        
        # Handle different types of results
        if isinstance(result, (int, float)):
            # For numbers, convert to string with appropriate precision
            return f"{result:.10g}"
        elif isinstance(result, complex):
            # For complex numbers, format as 'a + bj'
            return f"{result.real:.10g} + {result.imag:.10g}j"
        elif isinstance(result, bool):
            # For booleans, convert to lowercase string
            return str(result).lower()
        else:
            # For other types, convert to string
            return str(result)
    except ZeroDivisionError:
        # Handle division by zero
        return "Error: division by zero"
    except SyntaxError:
        # Handle syntax errors in the expression
        return "Error: invalid syntax"
    except NameError:
        # Handle undefined variables
        return "Error: undefined variable"
    except TypeError:
        # Handle type mismatches
        return "Error: type mismatch"
    except Exception as e:
        # Handle any other exceptions
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('10 / 2'))  # Should print: 5
    print(tentacle('10 / 0'))  # Should print: Error: division by zero
    print(tentacle('2 ** 3'))  # Should print: 8
    print(tentacle('(2 + 3) * 4'))  # Should print: 20
    print(tentacle('1 + 2j'))  # Should print: 1 + 2j
    print(tentacle('True and False'))  # Should print: false
    print(tentacle('invalid expression'))  # Should print: Error: invalid syntax
    print(tentacle('x + 2'))  # Should print: Error: undefined variable
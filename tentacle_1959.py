# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a mathematical expression given as a string.
    
    This function improves upon previous tentacles by adding support for
    more complex mathematical operations and providing better error handling.
    
    Args:
    expression (str): A string containing a mathematical expression.
    
    Returns:
    str: The result of the evaluated expression as a string, or an error message.
    
    Examples:
    >>> tentacle('2 + 2')
    '4'
    >>> tentacle('sin(pi/2)')
    '1.0'
    >>> tentacle('log10(100)')
    '2.0'
    """
    import math
    
    # Define a dictionary of mathematical functions
    math_functions = {
        'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
        'asin': math.asin, 'acos': math.acos, 'atan': math.atan,
        'sinh': math.sinh, 'cosh': math.cosh, 'tanh': math.tanh,
        'exp': math.exp, 'log': math.log, 'log10': math.log10,
        'sqrt': math.sqrt, 'pi': math.pi, 'e': math.e
    }
    
    try:
        # Create a safe evaluation environment
        safe_dict = {}
        safe_dict.update(math_functions)
        
        # Evaluate the expression using eval with the safe dictionary
        result = eval(expression, {"__builtins__": None}, safe_dict)
        
        # Convert the result to a string and return
        return str(result)
    
    except ZeroDivisionError:
        return "Error: Division by zero"
    except ValueError as e:
        return f"Error: Invalid value - {str(e)}"
    except NameError as e:
        return f"Error: Undefined variable or function - {str(e)}"
    except SyntaxError as e:
        return f"Error: Invalid syntax - {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('sin(pi/2)'))  # Should print: 1.0
    print(tentacle('log10(100)'))  # Should print: 2.0
    print(tentacle('1/0'))  # Should print: Error: Division by zero
    print(tentacle('sqrt(-1)'))  # Should print: Error: Invalid value - math domain error
    print(tentacle('unknown_function(5)'))  # Should print: Error: Undefined variable or function - name 'unknown_function' is not defined
    print(tentacle('2 + * 3'))  # Should print: Error: Invalid syntax - invalid syntax
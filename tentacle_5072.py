# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a mathematical expression given as a string.
    
    This function combines the ability to evaluate mathematical expressions
    from the first tentacle with improved error handling and additional
    mathematical operations support.

    Args:
    expression (str): A string containing a mathematical expression.
    
    Returns:
    str: The result of the evaluated expression as a string, or an error message.
    
    Example:
    >>> tentacle('2 + 2')
    '4'
    >>> tentacle('sin(pi/2)')
    '1.0'
    """
    try:
        # Import math module for additional mathematical functions
        import math
        
        # Define a dictionary of math functions for safe evaluation
        safe_math = {
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'sqrt': math.sqrt,
            'log': math.log,
            'exp': math.exp,
            'pi': math.pi,
            'e': math.e
        }
        
        # Evaluate the expression using the safe dictionary
        result = eval(expression, {"__builtins__": None}, safe_math)
        
        # Convert the result to a string with appropriate formatting
        if isinstance(result, float):
            return f"{result:.10g}"
        else:
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
    print(tentacle('log(e)'))  # Should print: 1.0
    print(tentacle('1/0'))  # Should print: Error: Division by zero
    print(tentacle('sqrt(-1)'))  # Should print: Error: Invalid value - math domain error
    print(tentacle('unknown_function(5)'))  # Should print: Error: Undefined variable or function - name 'unknown_function' is not defined
    print(tentacle('2 + * 3'))  # Should print: Error: Invalid syntax - invalid syntax
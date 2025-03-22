# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a mathematical expression given as a string.
    
    This function combines the ability to evaluate mathematical expressions
    with improved error handling and support for more complex expressions.
    
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
        # Import the math module for advanced mathematical functions
        import math
        
        # Define a dictionary of math functions for use in eval
        math_functions = {
            'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
            'asin': math.asin, 'acos': math.acos, 'atan': math.atan,
            'sinh': math.sinh, 'cosh': math.cosh, 'tanh': math.tanh,
            'exp': math.exp, 'log': math.log, 'sqrt': math.sqrt,
            'pi': math.pi, 'e': math.e
        }
        
        # Evaluate the expression using the math functions
        result = eval(expression, {"__builtins__": None}, math_functions)
        
        # Convert the result to a string with appropriate precision
        return f"{result:.10g}"
    except ZeroDivisionError:
        return "Error: Division by zero"
    except ValueError as e:
        return f"Error: Invalid value - {str(e)}"
    except NameError as e:
        return f"Error: Unknown function or variable - {str(e)}"
    except SyntaxError as e:
        return f"Error: Invalid syntax - {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('sin(pi/2)'))  # Should print: 1.0
    print(tentacle('log(e)'))  # Should print: 1.0
    print(tentacle('sqrt(16)'))  # Should print: 4.0
    print(tentacle('1/0'))  # Should print: Error: Division by zero
    print(tentacle('sin(x)'))  # Should print: Error: Unknown function or variable - name 'x' is not defined
    print(tentacle('2 +'))  # Should print: Error: Invalid syntax - invalid syntax
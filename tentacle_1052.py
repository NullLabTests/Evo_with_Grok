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
    >>> tentacle('sin(pi/2)')
    '1.0'
    """
    try:
        # Evaluate the expression using eval() with added safety measures
        result = eval(expression, {"__builtins__": None}, {"pi": 3.141592653589793, "e": 2.718281828459045, "sin": lambda x: math.sin(x), "cos": lambda x: math.cos(x), "tan": lambda x: math.tan(x)})
        
        # Convert the result to a string with proper formatting
        if isinstance(result, float):
            return f"{result:.10g}"
        else:
            return str(result)
    except Exception as e:
        # Return a detailed error message if evaluation fails
        return f"Error: {str(e)}"

# Import the math module for trigonometric functions
import math

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('5 * 3'))  # Should print: 15
    print(tentacle('(10 - 3) * 2'))  # Should print: 14
    print(tentacle('sin(pi/2)'))  # Should print: 1.0
    print(tentacle('cos(0)'))  # Should print: 1.0
    print(tentacle('tan(pi/4)'))  # Should print: 1.0
    print(tentacle('1/3'))  # Should print: 0.3333333333
    print(tentacle('sqrt(16)'))  # Should print: Error: name 'sqrt' is not defined
    print(tentacle('invalid expression'))  # Should print: Error: invalid syntax
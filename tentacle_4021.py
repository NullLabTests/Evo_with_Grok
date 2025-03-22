# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a mathematical expression given as a string.
    
    This function safely evaluates mathematical expressions and returns the result as a string.
    It uses a whitelist approach to allow only basic arithmetic operations and functions.
    
    Args:
    expression (str): A string containing a mathematical expression.
    
    Returns:
    str: The result of the evaluated expression as a string, or an error message if evaluation fails.
    
    Example:
    >>> tentacle('2 + 2')
    '4'
    >>> tentacle('sin(pi/2)')
    '1.0'
    """
    import math
    
    # Define a whitelist of allowed functions and operators
    allowed_names = {'sin': math.sin, 'cos': math.cos, 'tan': math.tan, 
                     'asin': math.asin, 'acos': math.acos, 'atan': math.atan,
                     'sqrt': math.sqrt, 'log': math.log, 'exp': math.exp,
                     'pi': math.pi, 'e': math.e}
    
    # Define allowed operators
    allowed_operators = set('+-*/()')
    
    try:
        # Compile the expression
        code = compile(expression, "<string>", "eval")
        
        # Check if all names used in the expression are in the whitelist
        for name in code.co_names:
            if name not in allowed_names:
                raise NameError(f"Function or constant '{name}' is not allowed")
        
        # Check if all characters in the expression are allowed
        for char in expression:
            if char.isalnum() or char.isspace() or char in allowed_operators:
                continue
            raise ValueError(f"Character '{char}' is not allowed")
        
        # Evaluate the expression using the whitelist
        result = eval(code, {"__builtins__": {}}, allowed_names)
        
        # Convert the result to a string
        return str(result)
    
    except Exception as e:
        # Return an error message if evaluation fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('sin(pi/2)'))  # Should print: 1.0
    print(tentacle('sqrt(16)'))  # Should print: 4.0
    print(tentacle('log(e)'))  # Should print: 1.0
    print(tentacle('2 ** 3'))  # Should print: 8
    print(tentacle('invalid_function(5)'))  # Should print: Error: Function or constant 'invalid_function' is not allowed
    print(tentacle('2 + 2; print("Hello")'))  # Should print: Error: Character ';' is not allowed
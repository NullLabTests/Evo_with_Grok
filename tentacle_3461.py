# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a mathematical expression given as a string.
    
    This function combines the ability to evaluate mathematical expressions
    with error handling and type conversion to ensure robust processing.

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
        # Import the math module to handle more complex mathematical functions
        import math
        
        # Evaluate the expression using eval with math module
        result = eval(expression, {"__builtins__": None}, {"math": math})
        
        # Convert the result to a string, handling potential complex numbers
        if isinstance(result, complex):
            return f"({result.real:.6g}{'+' if result.imag >= 0 else ''}{result.imag:.6g}j)"
        else:
            return f"{result:.6g}"
    except Exception as e:
        # Return a detailed error message if evaluation fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('sin(pi/2)'))  # Should print: 1
    print(tentacle('sqrt(16)'))  # Should print: 4
    print(tentacle('log(100, 10)'))  # Should print: 2
    print(tentacle('1/0'))  # Should print an error message
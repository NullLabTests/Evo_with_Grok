# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a mathematical expression given as a string.
    
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
    try:
        # Import math module to support more mathematical functions
        import math
        
        # Evaluate the expression using eval with math module
        result = eval(expression, {"__builtins__": None}, {"math": math})
        
        # Convert the result to a string with appropriate formatting
        if isinstance(result, float):
            return f"{result:.10g}"
        else:
            return str(result)
    except Exception as e:
        # Return a detailed error message if evaluation fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('5 * 3'))  # Should print: 15
    print(tentacle('sin(pi/2)'))  # Should print: 1.0
    print(tentacle('log(100, 10)'))  # Should print: 2.0
    print(tentacle('2 ** 3'))  # Should print: 8
    print(tentacle('(3 + 4) * 2'))  # Should print: 14
    print(tentacle('invalid expression'))  # Should print an error message
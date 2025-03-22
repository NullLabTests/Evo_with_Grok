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
    >>> tentacle('(3 * 4) / 2')
    '6.0'
    >>> tentacle('invalid expression')
    'Error: invalid syntax'
    """
    try:
        # Convert the expression to lowercase for consistency
        expression = expression.lower()
        
        # Replace common mathematical function names with their Python equivalents
        function_map = {
            'sqrt': 'math.sqrt',
            'sin': 'math.sin',
            'cos': 'math.cos',
            'tan': 'math.tan',
            'log': 'math.log',
            'exp': 'math.exp'
        }
        for key, value in function_map.items():
            expression = expression.replace(key, value)
        
        # Evaluate the expression using the math module
        import math
        result = str(eval(expression, {"__builtins__": None}, {"math": math}))
        return result
    except Exception as e:
        # Return an error message if evaluation fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('(3 * 4) / 2'))  # Should print: 6.0
    print(tentacle('sqrt(16)'))  # Should print: 4.0
    print(tentacle('sin(pi/2)'))  # Should print: 1.0
    print(tentacle('invalid expression'))  # Should print: Error: invalid syntax
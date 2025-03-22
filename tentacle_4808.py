# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a mathematical expression given as a string.
    
    This function improves upon the previous tentacles by:
    - Adding input validation to ensure the expression is a valid mathematical expression.
    - Using a safer evaluation method to prevent code injection.
    - Returning the result as a string, consistent with the original function.
    
    Args:
    expression (str): A string containing a mathematical expression.
    
    Returns:
    str: The result of the evaluated expression as a string, or an error message if evaluation fails.
    
    Example:
    >>> tentacle('2 + 2')
    '4'
    >>> tentacle('invalid expression')
    'Error: Invalid expression'
    """
    import re
    
    # Validate input: check if the expression contains only valid mathematical characters
    valid_chars = r'^[\d\s\+\-\*\/\(\)\.]+$'
    if not re.match(valid_chars, expression):
        return "Error: Invalid expression"
    
    try:
        # Use a safer evaluation method
        result = str(eval(expression, {"__builtins__": None}, {}))
        return result
    except Exception as e:
        # Return an error message if evaluation fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('3 * (4 + 5)'))  # Should print: 27
    print(tentacle('10 / 2'))  # Should print: 5.0
    print(tentacle('invalid expression'))  # Should print: Error: Invalid expression
    print(tentacle('__import__("os").system("ls")'))  # Should print: Error: Invalid expression
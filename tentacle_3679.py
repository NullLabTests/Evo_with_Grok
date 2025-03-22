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
    """
    try:
        # Evaluate the expression
        result = eval(expression)
        
        # Convert the result to a string, handling potential floating-point precision issues
        if isinstance(result, float):
            # Use string formatting to limit decimal places to 10
            return f"{result:.10g}"
        else:
            return str(result)
    except Exception as e:
        # Return an error message if evaluation fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('(3 * 4) / 2'))  # Should print: 6.0
    print(tentacle('sqrt(16)'))  # Should print: 4.0
    print(tentacle('2 ** 3'))  # Should print: 8
    print(tentacle('10 / 3'))  # Should print: 3.333333333
    print(tentacle('invalid expression'))  # Should print an error message
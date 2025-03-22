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
        # Evaluate the expression using eval() function
        result = eval(expression)
        
        # Convert the result to a string with appropriate formatting
        if isinstance(result, float):
            # For float results, use 10 decimal places to handle precision
            return f"{result:.10g}"
        else:
            # For other types, use str() conversion
            return str(result)
    except Exception as e:
        # Return a detailed error message if evaluation fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('3 * 4'))  # Should print: 12
    print(tentacle('10 / 3'))  # Should print: 3.333333333
    print(tentacle('sin(pi/2)'))  # Should print: 1.0
    print(tentacle('2 ** 3'))  # Should print: 8
    print(tentacle('(5 + 3) * 2'))  # Should print: 16
    print(tentacle('invalid expression'))  # Should print an error message
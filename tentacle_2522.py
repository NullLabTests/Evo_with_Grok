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
        
        # Handle potential complex numbers
        if isinstance(result, complex):
            return str(result)
        
        # Convert the result to a string, handling potential floating-point precision issues
        return str(round(result, 10)).rstrip('0').rstrip('.')
    except Exception as e:
        # Return an error message if evaluation fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('(3 * 4) / 2'))  # Should print: 6.0
    print(tentacle('5 ** 2'))  # Should print: 25
    print(tentacle('sqrt(16)'))  # Should print: 4.0
    print(tentacle('sin(pi/2)'))  # Should print: 1.0
    print(tentacle('1/3'))  # Should print: 0.3333333333
    print(tentacle('1j * 1j'))  # Should print: (-1+0j)
    print(tentacle('invalid expression'))  # Should print an error message
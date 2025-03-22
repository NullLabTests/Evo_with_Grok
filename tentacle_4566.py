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
        
        # Convert the result to a string, handling potential complex numbers
        if isinstance(result, complex):
            return f"{result.real:.10g}{result.imag:+.10g}j"
        else:
            return f"{result:.10g}"
    except Exception as e:
        # Return a detailed error message if evaluation fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('(3 * 4) / 2'))  # Should print: 6
    print(tentacle('2 ** 3'))  # Should print: 8
    print(tentacle('sin(pi/2)'))  # Should print: 1
    print(tentacle('1j * 1j'))  # Should print: -1+0j
    print(tentacle('1/0'))  # Should print an error message
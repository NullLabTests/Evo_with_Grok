# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a mathematical expression given as a string.
    
    This function combines the ability to evaluate mathematical expressions
    from the first tentacle with improved error handling and result formatting.
    
    Args:
    expression (str): A string containing a mathematical expression.
    
    Returns:
    str: The result of the evaluated expression as a string, or an error message.
    
    Example:
    >>> tentacle('2 + 2')
    '4'
    >>> tentacle('10 / 0')
    'Error: division by zero'
    """
    try:
        # Evaluate the expression
        result = eval(expression)
        
        # Format the result as a string, handling different types
        if isinstance(result, float):
            # For floats, limit to 10 decimal places to avoid very long results
            return f"{result:.10g}"
        elif isinstance(result, complex):
            # For complex numbers, format real and imaginary parts
            return f"({result.real:.10g}{result.imag:+.10g}j)"
        else:
            # For other types (int, bool), convert to string
            return str(result)
    except Exception as e:
        # Return a formatted error message if evaluation fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('10 / 3'))  # Should print: 3.333333333
    print(tentacle('2 ** 10'))  # Should print: 1024
    print(tentacle('1 + 2j'))  # Should print: (1+2j)
    print(tentacle('True and False'))  # Should print: False
    print(tentacle('10 / 0'))  # Should print: Error: division by zero
    print(tentacle('invalid expression'))  # Should print: Error: invalid syntax
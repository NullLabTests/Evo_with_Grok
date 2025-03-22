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
    >>> tentacle('3 * (4 + 5)')
    '27'
    """
    try:
        # Evaluate the expression
        result = eval(expression)
        
        # Handle different types of results
        if isinstance(result, (int, float)):
            # For numbers, convert to string with appropriate precision
            return f"{result:.10g}"
        elif isinstance(result, complex):
            # For complex numbers, format as 'a + bj'
            return f"{result.real:.10g} + {result.imag:.10g}j"
        elif isinstance(result, bool):
            # For boolean values, return as string
            return str(result)
        else:
            # For other types, convert to string
            return str(result)
    except Exception as e:
        # Return an error message if evaluation fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('3 * (4 + 5)'))  # Should print: 27
    print(tentacle('10 / 3'))  # Should print: 3.333333333
    print(tentacle('2 ** 3'))  # Should print: 8
    print(tentacle('1 + 2j'))  # Should print: 1 + 2j
    print(tentacle('True and False'))  # Should print: False
    print(tentacle('"Hello" + " World"'))  # Should print: Hello World
    print(tentacle('1/0'))  # Should print: Error: division by zero
# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a mathematical expression given as a string and return the result as a string.
    
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
        
        # Convert the result to a string with appropriate formatting
        if isinstance(result, float):
            # Use string formatting to handle floating-point numbers
            return f"{result:.10g}".rstrip('0').rstrip('.')
        else:
            # Convert other types (like integers) to strings
            return str(result)
    except Exception as e:
        # Return a detailed error message if evaluation fails
        return f"Error: Invalid expression - {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('(3 * 4) / 2'))  # Should print: 6
    print(tentacle('10 - 3.5'))  # Should print: 6.5
    print(tentacle('2 ** 3'))  # Should print: 8
    print(tentacle('(5 + 3) * 2'))  # Should print: 16
    print(tentacle('invalid expression'))  # Should print an error message
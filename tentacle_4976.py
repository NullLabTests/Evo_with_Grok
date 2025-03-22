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
        
        # Convert the result to a string, handling both integers and floats
        if isinstance(result, int):
            return str(result)
        elif isinstance(result, float):
            # Use string formatting to limit decimal places to 10
            return f"{result:.10g}"
        else:
            # If the result is neither an int nor a float, return its string representation
            return str(result)
    except Exception as e:
        # Return a more detailed error message if evaluation fails
        return f"Error evaluating expression: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('(3 * 4) / 2'))  # Should print: 6.0
    print(tentacle('5 ** 2'))  # Should print: 25
    print(tentacle('sin(pi/2)'))  # Should print: 1.0 (assuming math module is imported)
    print(tentacle('1/0'))  # Should print: Error evaluating expression: division by zero
    print(tentacle('invalid expression'))  # Should print: Error evaluating expression: ...
# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a mathematical expression given as a string.
    
    This function combines the functionality of evaluating mathematical expressions
    with improved error handling and type conversion.

    Args:
    expression (str): A string containing a mathematical expression.

    Returns:
    str: The result of the evaluated expression as a string, or an error message.

    Example:
    >>> tentacle('2 + 2')
    '4'
    >>> tentacle('3 * (4 + 5)')
    '27'
    """
    try:
        # Evaluate the expression
        result = eval(expression)
        
        # Convert the result to the appropriate string representation
        if isinstance(result, float):
            # For floating-point numbers, use a fixed precision to avoid issues with representation
            return f"{result:.10g}"
        else:
            # For other types, use the standard string conversion
            return str(result)
    except Exception as e:
        # Return a detailed error message if evaluation fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('3 * (4 + 5)'))  # Should print: 27
    print(tentacle('10 / 3'))  # Should print: 3.333333333
    print(tentacle('2 ** 3'))  # Should print: 8
    print(tentacle('invalid expression'))  # Should print an error message
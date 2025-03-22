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
    >>> tentacle('(3 + 5) * 2')
    '16'
    """
    try:
        # Evaluate the expression and convert the result to a string
        result = str(eval(expression))
        return result
    except Exception as e:
        # Return a more detailed error message if evaluation fails
        return f"Error evaluating expression: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('(3 + 5) * 2'))  # Should print: 16
    print(tentacle('10 / 0'))  # Should print an error message
    print(tentacle('invalid expression'))  # Should print an error message
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
        
        # Convert the result to a string, handling both integer and float results
        if isinstance(result, int):
            return str(result)
        elif isinstance(result, float):
            # Remove trailing zeros for cleaner output
            return str(result).rstrip('0').rstrip('.') if '.' in str(result) else str(result)
        else:
            return f"Error: Unexpected result type {type(result)}"
    except Exception as e:
        # Return a detailed error message if evaluation fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('(3 * 4) / 2'))  # Should print: 6.0
    print(tentacle('5 - 3'))  # Should print: 2
    print(tentacle('10 / 2'))  # Should print: 5.0
    print(tentacle('2 ** 3'))  # Should print: 8
    print(tentacle('(2 + 3) * 4'))  # Should print: 20
    print(tentacle('invalid expression'))  # Should print an error message
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
        if isinstance(result, int):
            return str(result)
        elif isinstance(result, float):
            # Use scientific notation for very large or very small numbers
            if abs(result) < 1e-4 or abs(result) > 1e15:
                return f"{result:.2e}"
            else:
                return f"{result:.6f}".rstrip('0').rstrip('.')
        else:
            return str(result)
    except Exception as e:
        # Return a detailed error message if evaluation fails
        return f"Error: Invalid expression - {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('(3 * 4) / 2'))  # Should print: 6.0
    print(tentacle('2 ** 10'))  # Should print: 1024
    print(tentacle('1 / 3'))  # Should print: 0.333333
    print(tentacle('1e20 * 1e-20'))  # Should print: 1.00
    print(tentacle('1e-20 / 1e20'))  # Should print: 1.00e-40
    print(tentacle('invalid expression'))  # Should print an error message
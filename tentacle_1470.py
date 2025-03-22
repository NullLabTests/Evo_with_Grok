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
    >>> tentacle('3 * (4 + 5)')
    '27'
    """
    try:
        # Evaluate the expression
        result = eval(expression)
        
        # Convert the result to a string, handling potential non-numeric results
        if isinstance(result, (int, float)):
            return str(result)
        else:
            return str(result)
    except Exception as e:
        # Return a detailed error message if evaluation fails
        return f"Error: Unable to evaluate the expression. {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('3 * (4 + 5)'))  # Should print: 27
    print(tentacle('10 / 2'))  # Should print: 5.0
    print(tentacle('2 ** 3'))  # Should print: 8
    print(tentacle('invalid expression'))  # Should print an error message
# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a mathematical expression given as a string and provide a detailed result.

    Args:
    expression (str): A string containing a mathematical expression.

    Returns:
    str: The result of the evaluated expression as a string, including the original expression.

    Example:
    >>> tentacle('2 + 2')
    '2 + 2 = 4'
    """
    try:
        # Evaluate the expression
        result = eval(expression)
        
        # Format the result string to include the original expression and the result
        formatted_result = f"{expression} = {result}"
        
        return formatted_result
    except Exception as e:
        # Return an error message if evaluation fails, including the original expression
        return f"Error evaluating '{expression}': {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 2 + 2 = 4
    print(tentacle('3 * 4'))  # Should print: 3 * 4 = 12
    print(tentacle('10 / 2'))  # Should print: 10 / 2 = 5.0
    print(tentacle('2 ** 3'))  # Should print: 2 ** 3 = 8
    print(tentacle('(5 + 3) * 2'))  # Should print: (5 + 3) * 2 = 16
    print(tentacle('invalid expression'))  # Should print an error message
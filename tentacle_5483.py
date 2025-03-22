# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a mathematical expression given as a string.
    
    Args:
    expression (str): A string containing a mathematical expression.
    
    Returns:
    str: The result of the evaluated expression as a string or an error message.
    
    Example:
    >>> tentacle('2 + 2')
    '4'
    >>> tentacle('If A implies B and B implies C, then A implies C.')
    'Error: Invalid mathematical expression'
    """
    try:
        # Convert the expression to lowercase for consistency
        expression = expression.lower()
        
        # Check if the expression is a valid mathematical expression
        if any(char.isdigit() for char in expression) and any(char in '+-*/()' for char in expression):
            # Evaluate the expression and convert the result to a string
            result = str(eval(expression))
            return result
        else:
            # Return an error message for invalid mathematical expressions
            return "Error: Invalid mathematical expression"
    except Exception as e:
        # Return an error message if evaluation fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('3 * 4'))  # Should print: 12
    print(tentacle('(5 + 3) * 2'))  # Should print: 16
    print(tentacle('If A implies B and B implies C, then A implies C.'))  # Should print: Error: Invalid mathematical expression
    print(tentacle('2 + x'))  # Should print: Error: name 'x' is not defined
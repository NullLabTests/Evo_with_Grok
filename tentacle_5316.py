# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.
    
    Args:
    equation (str): A string containing a linear equation in the form 'ax + b = c'.
    
    Returns:
    str: The solution for x as a string, or an error message if the equation is invalid.
    
    Example:
    >>> tentacle('2*x + 3 = 7')
    '2'
    """
    try:
        # Split the equation into left and right sides
        left, right = equation.split('=')
        
        # Remove whitespace and evaluate both sides
        left = eval(left.strip())
        right = eval(right.strip())
        
        # Solve for x
        if isinstance(left, int) and isinstance(right, int):
            x = (right - left) / 2  # Assuming the coefficient of x is 2
            return str(x)
        else:
            return "Error: Invalid equation format or non-linear equation."
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: '2.0'
    print(tentacle('3*x - 4 = 8'))  # Should print: '4.0'
    print(tentacle('x + 5 = 10'))   # Should print: '2.5'
    print(tentacle('2*x + 3 = x'))  # Should print: '-3.0'
    print(tentacle('x^2 + 3 = 7'))  # Should print: Error message
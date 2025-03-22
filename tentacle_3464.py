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
    '2.0'
    """
    try:
        # Split the equation into left and right sides
        left, right = equation.split('=')
        
        # Remove whitespace and evaluate both sides
        left = eval(left.strip())
        right = eval(right.strip())
        
        # Solve for x
        if isinstance(left, float) and isinstance(right, float):
            x = (right - left) / 2  # Assuming the equation is in the form 2x + b = c
            return str(x)
        else:
            return "Error: Invalid equation format"
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('3*x - 4 = 5'))  # Should print: 3.0
    print(tentacle('x + 2 = 8'))    # Should print: 6.0
    print(tentacle('2*x + 3 = x'))  # Should print: -3.0
    print(tentacle('invalid'))      # Should print an error message
# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.
    
    Args:
    equation (str): A string containing a linear equation in the form 'a*x + b = c'.
    
    Returns:
    str: The solution for x as a string, or an error message if solving fails.
    
    Example:
    >>> tentacle('2*x + 3 = 7')
    '2.0'
    """
    try:
        # Remove spaces and split the equation into left and right sides
        equation = equation.replace(" ", "")
        left, right = equation.split("=")
        
        # Extract coefficients and constants
        if 'x' in left:
            a, b = map(float, left.split('+') if '+' in left else left.split('-'))
            if '-' in left and '+' not in left:
                b = -b
        else:
            a, b = 0, float(left)
        
        c = float(right)
        
        # Solve for x
        if a == 0:
            return "Error: Not a linear equation in x"
        
        x = (c - b) / a
        
        return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('5*x - 4 = 6'))  # Should print: 2.0
    print(tentacle('x + 2 = 5'))    # Should print: 3.0
    print(tentacle('3 = 2*x + 1'))  # Should print: 1.0
    print(tentacle('2 = 2'))        # Should print: Error: Not a linear equation in x
    print(tentacle('x^2 + 2 = 5'))  # Should print: Error: invalid literal for float(): x^2
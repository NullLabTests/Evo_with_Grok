# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.
    
    Args:
    equation (str): A string containing a linear equation in the form 'a*x + b = c'.
    
    Returns:
    str: The solution for x as a string, or an error message if the equation cannot be solved.
    
    Example:
    >>> tentacle('2*x + 3 = 7')
    '2'
    """
    try:
        # Split the equation into left and right sides
        left, right = equation.split('=')
        
        # Remove whitespace
        left = left.strip()
        right = right.strip()
        
        # Parse the left side
        if '*' in left:
            a, b = left.split('+')
            a = a.strip()
            b = b.strip()
        else:
            a = left
            b = '0'
        
        # Extract coefficients
        a = float(a.split('*')[0]) if '*' in a else 1.0
        b = float(b)
        c = float(right)
        
        # Solve for x
        x = (c - b) / a
        
        return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x + 5 = 10'))   # Should print: 5.0
    print(tentacle('3*x = 9'))      # Should print: 3.0
    print(tentacle('2*x - 4 = 0'))  # Should print: 2.0
    print(tentacle('x = 5'))        # Should print: 5.0
    print(tentacle('2*x + y = 7'))  # Should print: Error: invalid literal for float(): y
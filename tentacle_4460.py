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
        
        # Parse the left side to extract coefficients
        if 'x' in left:
            if '*' in left:
                a, _ = left.split('*')
                a = float(a)
            else:
                a = float(left.replace('x', '1'))
        else:
            a = 0
        
        # Extract the constant term on the left side
        b = 0
        if '+' in left:
            b = float(left.split('+')[1])
        elif '-' in left and 'x' in left.split('-')[0]:
            b = -float(left.split('-')[1])
        
        # Convert right side to float
        c = float(right)
        
        # Solve for x
        if a == 0:
            return "Error: Cannot solve for x (a = 0)"
        x = (c - b) / a
        
        return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('5*x - 2 = 8'))  # Should print: 2.0
    print(tentacle('x + 4 = 10'))   # Should print: 6.0
    print(tentacle('3*x = 9'))      # Should print: 3.0
    print(tentacle('2 = 2'))        # Should print: Error: Cannot solve for x (a = 0)
    print(tentacle('invalid'))      # Should print: Error: ...
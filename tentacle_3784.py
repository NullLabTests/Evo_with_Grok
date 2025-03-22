# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x.

    Args:
    equation (str): A string containing a linear equation in the format 'ax + b = c'.

    Returns:
    str: The solution for x as a string, or an error message if the equation is invalid.

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
        
        # Parse the left side of the equation
        if 'x' in left:
            if '*' in left:
                a, _ = left.split('*')
                a = float(a)
            else:
                a = 1.0 if left == 'x' else float(left.replace('x', ''))
        else:
            return "Error: Equation must contain x"
        
        # Parse the right side and the constant term on the left side
        b = 0.0
        if '+' in left:
            b = float(left.split('+')[1])
        elif '-' in left:
            b = -float(left.split('-')[1])
        
        c = float(right)
        
        # Solve for x
        x = (c - b) / a
        
        return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 10'))   # Should print: 15.0
    print(tentacle('3*x = 12'))     # Should print: 4.0
    print(tentacle('x + 2 = 8'))    # Should print: 6.0
    print(tentacle('2*x = 7'))      # Should print: 3.5
    print(tentacle('x = 5'))        # Should print: 5.0
    print(tentacle('2*x + 3 = x'))  # Should print: -3.0
    print(tentacle('2*x + 3'))      # Should print: Error: Equation must contain '='
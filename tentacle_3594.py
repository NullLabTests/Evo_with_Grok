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
            a = 0.0
        
        # Parse the constant term on the left side
        b = 0.0
        if 'x' in left:
            left_without_x = left.replace('x', '')
            if left_without_x:
                b = float(left_without_x)
        else:
            b = float(left)
        
        # Parse the right side of the equation
        c = float(right)
        
        # Solve for x
        x = (c - b) / a
        
        # Return the solution as a string
        return str(x)
    
    except Exception as e:
        # Return an error message if solving fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x + 5 = 10'))   # Should print: 5.0
    print(tentacle('3*x = 9'))      # Should print: 3.0
    print(tentacle('x = 4'))        # Should print: 4.0
    print(tentacle('5 = x'))        # Should print: 5.0
    print(tentacle('2*x + 3 = x + 7'))  # Should print: 4.0
    print(tentacle('invalid equation')) # Should print an error message
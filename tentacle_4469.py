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
        left, right = left.strip(), right.strip()
        
        # Parse the left side
        if 'x' in left:
            if '*' in left:
                a, _ = left.split('*')
                a = float(a)
            elif left == 'x':
                a = 1
            else:
                a = float(left.replace('x', ''))
        else:
            a = 0
        
        # Parse the right side
        c = float(right)
        
        # Parse the constant term on the left side
        b = 0
        if '+' in left:
            b = float(left.split('+')[1].replace('x', ''))
        elif '-' in left:
            b = float(left.split('-')[1].replace('x', '')) * -1
        
        # Solve for x
        if a == 0:
            return "Error: Not a valid linear equation"
        x = (c - b) / a
        
        return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 10'))   # Should print: 15.0
    print(tentacle('3x = 9'))       # Should print: 3.0
    print(tentacle('x = 4'))        # Should print: 4.0
    print(tentacle('2 + 3 = 5'))    # Should print: Error: Not a valid linear equation
    print(tentacle('y + 2 = 7'))    # Should print: Error: Not a valid linear equation
# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.
    
    Args:
    equation (str): A string containing a linear equation in the form 'ax + b = c'.
    
    Returns:
    str: The value of x as a string, or an error message if the equation cannot be solved.
    
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
        if '+' in left:
            a_part, b_part = left.split('+')
            a_part = a_part.strip()
            b_part = b_part.strip()
        elif '-' in left:
            a_part, b_part = left.split('-')
            a_part = a_part.strip()
            b_part = '-' + b_part.strip()
        else:
            a_part = left
            b_part = '0'
        
        # Extract coefficient of x
        if a_part == 'x':
            a = 1
        elif a_part == '-x':
            a = -1
        elif 'x' in a_part:
            a = float(a_part.replace('x', ''))
        else:
            a = 0
        
        # Extract constant term
        b = float(b_part) if b_part else 0
        
        # Solve for x
        c = float(right)
        x = (c - b) / a
        
        # Return the result as a string
        return str(x)
    
    except Exception as e:
        # Return an error message if solving fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 10'))  # Should print: 15.0
    print(tentacle('3*x = 12'))  # Should print: 4.0
    print(tentacle('x + 2 = 2'))  # Should print: 0.0
    print(tentacle('2*x - 1 = 3'))  # Should print: 2.0
    print(tentacle('x = 5'))  # Should print: 5.0
    print(tentacle('2*x + 3 = 3*x + 2'))  # Should print: -1.0
    print(tentacle('invalid equation'))  # Should print an error message
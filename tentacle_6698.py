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
        
        # Parse the left side
        if '+' in left:
            a_part, b_part = left.split('+')
        elif '-' in left:
            a_part, b_part = left.split('-')
            b_part = '-' + b_part
        else:
            a_part = left
            b_part = '0'
        
        # Extract coefficient of x
        a_part = a_part.strip()
        if a_part == 'x':
            a = 1
        elif a_part == '-x':
            a = -1
        elif a_part.endswith('x'):
            a = float(a_part[:-1])
        else:
            return "Error: Invalid equation format"
        
        # Extract constant term
        b = float(b_part)
        
        # Solve for x
        c = float(right)
        x = (c - b) / a
        
        return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 10'))  # Should print: 15.0
    print(tentacle('-3*x = 9'))  # Should print: -3.0
    print(tentacle('2x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x = 5'))  # Should print: 5.0
    print(tentacle('2*x + y = 7'))  # Should print: Error: Invalid equation format
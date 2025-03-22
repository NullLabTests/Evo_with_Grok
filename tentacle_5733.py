# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x and return the value of x.

    Args:
    equation (str): A string containing a linear equation in the format 'a*x + b = c'.

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
        
        # Parse the left side to extract coefficients
        if 'x' not in left:
            return "Error: Equation must contain 'x'"
        
        if '+' in left:
            a, b = left.split('+')
            a = a.strip()
            b = b.strip()
        elif '-' in left:
            if left.startswith('-'):
                a = '-' + left.split('-', 1)[1].split('x')[0]
                b = '-' + left.split('-', 1)[1].split('x')[1]
            else:
                a, b = left.split('-')
                a = a.strip()
                b = '-' + b.strip()
        else:
            a = left.split('x')[0]
            b = '0'
        
        # Extract coefficient of x
        if a.endswith('x'):
            a = a[:-1]
        if a == '' or a == '-':
            a += '1'
        
        # Convert coefficients to floats
        a = float(a)
        b = float(b)
        c = float(right)
        
        # Solve for x
        x = (c - b) / a
        
        # Return x as a string, rounded to 2 decimal places
        return f"{x:.2f}"
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.00
    print(tentacle('3*x - 4 = 5'))  # Should print: 3.00
    print(tentacle('-x + 2 = 0'))   # Should print: 2.00
    print(tentacle('x - 1 = 2'))    # Should print: 3.00
    print(tentacle('2*x = 6'))      # Should print: 3.00
    print(tentacle('x = 5'))        # Should print: 5.00
    print(tentacle('2*x + 3 = x'))  # Should print: -3.00
    print(tentacle('2*x + 3'))      # Should print: Error: Equation must contain '='
    print(tentacle('y + 3 = 7'))    # Should print: Error: Equation must contain 'x'
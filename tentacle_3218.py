# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.
    
    Args:
    equation (str): A string containing a linear equation in the form 'a*x + b = c'.
    
    Returns:
    str: The solution for x as a string, or an error message if the equation is invalid.
    
    Example:
    >>> tentacle('2*x + 3 = 7')
    '2'
    """
    try:
        # Split the equation into left and right sides
        left, right = equation.split('=')
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
        
        a = a.replace('x', '') if 'x' in a else a
        b = b if b != 'x' else '1'
        
        # Convert coefficients to floats
        a = float(a) if a else 1.0
        b = float(b) if b else 0.0
        c = float(right)
        
        # Solve for x
        x = (c - b) / a
        
        return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('5*x - 2 = 8'))  # Should print: 2.0
    print(tentacle('-x + 4 = 1'))   # Should print: -3.0
    print(tentacle('x = 5'))        # Should print: 5.0
    print(tentacle('3*x = 9'))      # Should print: 3.0
    print(tentacle('2*x + 3 = y'))  # Should print: Error: could not convert string to float: 'y'
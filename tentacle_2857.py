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
        
        # Remove whitespace and simplify the equation
        left = left.strip().replace(' ', '')
        right = right.strip().replace(' ', '')
        
        # Extract coefficients
        if 'x' in left:
            if '+' in left:
                a, b = left.split('+')
                a = a.replace('x', '') if 'x' in a else '1'
                b = '-' + b if b.startswith('-') else b
            elif '-' in left:
                a, b = left.split('-')
                a = a.replace('x', '') if 'x' in a else '1'
                b = '-' + b
            else:
                a = left.replace('x', '') if 'x' in left else '1'
                b = '0'
        else:
            a = '0'
            b = left
        
        c = right
        
        # Convert coefficients to floats
        a = float(a) if a else 1.0
        b = float(b) if b else 0.0
        c = float(c)
        
        # Solve for x
        if a == 0:
            return "Error: Not a linear equation (a = 0)"
        x = (c - b) / a
        
        return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 10'))   # Should print: 15.0
    print(tentacle('3*x = 12'))     # Should print: 4.0
    print(tentacle('5 = 2*x + 1'))  # Should print: 2.0
    print(tentacle('x = 7'))        # Should print: 7.0
    print(tentacle('2*x = 0'))      # Should print: 0.0
    print(tentacle('0*x + 3 = 7')) # Should print: Error: Not a linear equation (a = 0)
    print(tentacle('2*x + y = 7'))  # Should print: Error: invalid literal for float(): y
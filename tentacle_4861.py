# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x and return the value of x.
    
    Args:
    equation (str): A string containing a linear equation in the format 'ax + b = c'.
    
    Returns:
    str: The value of x as a string, or an error message if the equation is invalid or not linear.
    
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
        
        # Extract coefficients and constant
        if 'x' in left:
            if '+' in left:
                a, b = left.split('+')
                a = a.replace('x', '') if 'x' in a else '1' if a == 'x' else a
                b = b if 'x' not in b else '0'
            elif '-' in left:
                a, b = left.split('-')
                a = a.replace('x', '') if 'x' in a else '1' if a == 'x' else a
                b = '-' + b if 'x' not in b else '-1' if b == 'x' else '0'
            else:
                a = left.replace('x', '') if 'x' in left else '1' if left == 'x' else left
                b = '0'
        else:
            a = '0'
            b = left
        
        c = right
        
        # Convert to float
        a = float(a) if a else 0
        b = float(b) if b else 0
        c = float(c) if c else 0
        
        # Solve for x
        if a == 0:
            return "Error: Not a linear equation in x"
        x = (c - b) / a
        
        return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('5*x - 2 = 8'))  # Should print: 2.0
    print(tentacle('-x + 4 = 1'))   # Should print: 3.0
    print(tentacle('3 = 3'))        # Should print: Error: Not a linear equation in x
    print(tentacle('x^2 + 2 = 5'))  # Should print: Error: invalid syntax
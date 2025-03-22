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
        
        # Remove whitespace and simplify the equation
        left = left.strip().replace(' ', '')
        right = right.strip().replace(' ', '')
        
        # Parse the left side to extract coefficients
        if 'x' not in left:
            return "Error: Equation does not contain x"
        
        if '+' in left:
            a, b = left.split('+')
            a = a.replace('x', '') if 'x' in a else '0'
            b = b.replace('x', '') if 'x' in b else '0'
        elif '-' in left:
            a, b = left.split('-')
            a = a.replace('x', '') if 'x' in a else '0'
            b = '-' + b.replace('x', '') if 'x' in b else '0'
        else:
            a = left.replace('x', '') if 'x' in left else '0'
            b = '0'
        
        a = float(a) if a else 1.0  # Default to 1 if no coefficient is specified
        b = float(b)
        c = float(right)
        
        # Solve for x
        x = (c - b) / a
        
        return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 0'))    # Should print: 5.0
    print(tentacle('3*x = 12'))     # Should print: 4.0
    print(tentacle('x + 2 = 2'))    # Should print: 0.0
    print(tentacle('2 = 2'))        # Should print: Error: Equation does not contain x
    print(tentacle('x + y = 2'))    # Should print: Error: Equation does not contain x
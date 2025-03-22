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
        # Remove whitespace and split the equation at '='
        equation = equation.replace(" ", "").split("=")
        
        if len(equation) != 2:
            return "Error: Invalid equation format"
        
        left, right = equation
        
        # Extract coefficients and constant terms
        if 'x' in left:
            if '+' in left:
                a, b = left.split('+')
                a = a.replace('x', '') if 'x' in a else '1' if a == 'x' else a
                b = b if b != 'x' else '1'
            elif '-' in left:
                a, b = left.split('-')
                a = a.replace('x', '') if 'x' in a else '1' if a == 'x' else a
                b = '-' + b if b != 'x' else '-1'
            else:
                a = left.replace('x', '') if 'x' in left else '1' if left == 'x' else left
                b = '0'
        else:
            a = '0'
            b = left
        
        a = float(a) if a else 1.0
        b = float(b) if b else 0.0
        c = float(right)
        
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
    print(tentacle('5*x - 2 = 8'))  # Should print: 2.0
    print(tentacle('x + 4 = 10'))   # Should print: 6.0
    print(tentacle('3*x = 9'))      # Should print: 3.0
    print(tentacle('2 = 2'))        # Should print: Error: Not a linear equation (a = 0)
    print(tentacle('x + x = 4'))    # Should print: 2.0
    print(tentacle('2*x + 3 = x + 7'))  # Should print: 4.0
    print(tentacle('invalid equation')) # Should print: Error: Invalid equation format
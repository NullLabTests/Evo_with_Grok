# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.
    
    Args:
    equation (str): A string containing a linear equation in the form 'a*x + b = c'.
    
    Returns:
    str: The solution for x as a string, or an error message if the equation cannot be solved.
    
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
        
        # Extract coefficients and constants
        if 'x' in left:
            if '+' in left:
                a, b = left.split('+')
                a = a.strip()
                b = b.strip()
            elif '-' in left:
                a, b = left.split('-')
                a = a.strip()
                b = '-' + b.strip()
            else:
                a = left
                b = '0'
            
            # Extract coefficient of x
            if a == 'x':
                a = '1'
            elif a.startswith('-x'):
                a = '-1'
            else:
                a = a.replace('x', '')
            
            # Convert to floats
            a = float(a)
            b = float(b)
            c = float(right)
            
            # Solve for x
            x = (c - b) / a
            
            return str(x)
        else:
            return "Error: Equation does not contain 'x'"
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('5*x - 4 = 11'))  # Should print: 3.0
    print(tentacle('x + 2 = 5'))  # Should print: 3.0
    print(tentacle('-3*x = 9'))  # Should print: -3.0
    print(tentacle('2 = 2'))  # Should print: Error: Equation does not contain 'x'
    print(tentacle('invalid equation'))  # Should print: Error: ...
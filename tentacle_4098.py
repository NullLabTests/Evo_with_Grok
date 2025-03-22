# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.
    
    Args:
    equation (str): A string containing a linear equation in the form 'ax + b = c'.
    
    Returns:
    str: The solution for x as a string, or an error message if solving fails.
    
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
        if 'x' in left:
            if '+' in left:
                a, b = left.split('+')
                a = float(a.replace('x', '')) if 'x' in a else float(a)
                b = float(b.replace('x', '')) if 'x' in b else float(b)
            elif '-' in left:
                a, b = left.split('-')
                a = float(a.replace('x', '')) if 'x' in a else float(a)
                b = -float(b.replace('x', '')) if 'x' in b else -float(b)
            else:
                a = float(left.replace('x', ''))
                b = 0
        else:
            a = 0
            b = float(left)
        
        # Parse the right side
        c = float(right)
        
        # Solve for x
        if a == 0 and b == c:
            return 'All real numbers'
        elif a == 0:
            return 'No solution'
        else:
            x = (c - b) / a
            return str(x)
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 10'))  # Should print: 15.0
    print(tentacle('3*x = 12'))  # Should print: 4.0
    print(tentacle('0*x + 5 = 5'))  # Should print: All real numbers
    print(tentacle('0*x + 5 = 10'))  # Should print: No solution
    print(tentacle('2*x + 3 = 7*x'))  # Should print: Error: invalid syntax
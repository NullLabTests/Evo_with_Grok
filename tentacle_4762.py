# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.

    Args:
    equation (str): A string containing a linear equation in the form 'ax + b = c'.

    Returns:
    str: The solution for x as a string.

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
        
        # Extract coefficients
        if 'x' in left:
            if '*' in left:
                a = float(left.split('*')[0])
            else:
                a = 1.0 if left == 'x' else float(left.replace('x', ''))
            b = 0.0 if '+' not in left and '-' not in left else float(left.split('x')[1] or '0')
        else:
            a = 0.0
            b = float(left)
        
        c = float(right)
        
        # Solve for x
        if a == 0:
            if b == c:
                return 'All real numbers'
            else:
                return 'No solution'
        else:
            x = (c - b) / a
            return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 0'))  # Should print: 5.0
    print(tentacle('3x = 9'))  # Should print: 3.0
    print(tentacle('x = 4'))  # Should print: 4.0
    print(tentacle('0 = 0'))  # Should print: All real numbers
    print(tentacle('0 = 1'))  # Should print: No solution
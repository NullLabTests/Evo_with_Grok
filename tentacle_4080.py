# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.
    
    Args:
    equation (str): A string containing a linear equation in the form 'a*x + b = c'.
    
    Returns:
    str: The solution for x as a string, or an error message if solving fails.
    
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
            a_part = a_part.strip()
            b_part = b_part.strip()
        elif '-' in left:
            a_part, b_part = left.split('-')
            a_part = a_part.strip()
            b_part = '-' + b_part.strip()
        else:
            a_part = left
            b_part = '0'
        
        # Extract coefficients
        if 'x' in a_part:
            a = float(a_part.replace('x', '').strip() or '1')
        else:
            a = float(a_part)
            b_part = left
            b = float(b_part)
        
        if 'x' in b_part:
            b = float(b_part.replace('x', '').strip() or '1')
        else:
            b = float(b_part)
        
        # Calculate x
        c = float(right)
        x = (c - b) / a
        
        # Return the result as a string
        return str(x)
    
    except Exception as e:
        # Return an error message if solving fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('5*x - 4 = 6'))  # Should print: 2.0
    print(tentacle('x + 2 = 5'))  # Should print: 3.0
    print(tentacle('3*x = 9'))  # Should print: 3.0
    print(tentacle('2*x + 3 = x + 5'))  # Should print: 2.0
    print(tentacle('invalid equation'))  # Should print an error message
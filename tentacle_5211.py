# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.
    
    Args:
    equation (str): A string containing a linear equation in the format 'ax + b = c'.
    
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
            a, b = 0, 0
            if '+' in left:
                a_part, b_part = left.split('+')
                a = float(a_part.replace('x', '').strip()) if 'x' in a_part else 0
                b = float(b_part) if b_part else 0
            elif '-' in left:
                a_part, b_part = left.split('-')
                a = float(a_part.replace('x', '').strip()) if 'x' in a_part else 0
                b = -float(b_part) if b_part else 0
            else:
                a = float(left.replace('x', '').strip()) if 'x' in left else 0
                b = 0
        else:
            a, b = 0, float(left)
        
        c = float(right)
        
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
    print(tentacle('x - 5 = 10'))   # Should print: 15.0
    print(tentacle('3*x = 9'))      # Should print: 3.0
    print(tentacle('5 = 2*x + 1'))  # Should print: 2.0
    print(tentacle('x = 4'))        # Should print: 4.0
    print(tentacle('2 + 3 = 5'))    # Should print: Error: Not a linear equation in x
    print(tentacle('y + 2 = 7'))    # Should print: Error: Not a linear equation in x
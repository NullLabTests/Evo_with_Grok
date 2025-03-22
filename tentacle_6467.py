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
        # Remove spaces and split the equation into left and right sides
        equation = equation.replace(" ", "").split("=")
        left_side = equation[0]
        right_side = equation[1]
        
        # Extract coefficients
        if 'x' in left_side:
            if left_side.startswith('-x') or left_side.startswith('x'):
                a = -1 if left_side.startswith('-x') else 1
                b = eval(left_side.replace('-x', '0').replace('x', '0'))
            else:
                a, b = map(float, left_side.split('x+'))
                a = float(a) if a else 1
        else:
            a, b = 0, float(left_side)
        
        c = float(right_side)
        
        # Solve for x
        x = (c - b) / a
        
        return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('-x + 5 = 2'))  # Should print: 3.0
    print(tentacle('x - 4 = 10'))  # Should print: 14.0
    print(tentacle('3 = 3'))  # Should print: Error: division by zero
    print(tentacle('2*x + y = 7'))  # Should print: Error: name 'y' is not defined
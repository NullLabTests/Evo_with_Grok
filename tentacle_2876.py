# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x.
    
    Args:
    equation (str): A string containing a linear equation in the form 'ax + b = c'.
    
    Returns:
    str: The solution for x as a string.
    
    Example:
    >>> tentacle('2*x + 3 = 7')
    '2'
    """
    try:
        # Remove spaces and split the equation at '='
        equation = equation.replace(" ", "").split("=")
        
        # Parse left and right sides of the equation
        left_side = equation[0]
        right_side = equation[1]
        
        # Extract coefficients and constant
        if 'x' in left_side:
            if left_side.startswith('-x') or left_side.startswith('x'):
                a = -1 if left_side.startswith('-x') else 1
                b = 0 if len(left_side) == 1 or len(left_side) == 2 else eval(left_side[1:] if left_side.startswith('x') else left_side[2:])
            else:
                a, b = map(float, left_side.split('x'))
                b = b if '+' in left_side else -b
        else:
            a = 0
            b = float(left_side)
        
        c = float(right_side)
        
        # Solve for x
        if a == 0:
            if b == c:
                return 'Infinite solutions'
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
    print(tentacle('-x + 2 = 10'))  # Should print: -8.0
    print(tentacle('3 = 3'))  # Should print: Infinite solutions
    print(tentacle('3 = 4'))  # Should print: No solution
    print(tentacle('2x + 3 = 7'))  # Should print: 2.0
    print(tentacle('-x = 5'))  # Should print: -5.0
    print(tentacle('x = 10'))  # Should print: 10.0
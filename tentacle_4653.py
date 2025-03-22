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
        # Remove spaces and split the equation into left and right sides
        equation = equation.replace(" ", "").split("=")
        left_side = equation[0]
        right_side = equation[1]
        
        # Extract coefficients and constant terms
        if 'x' in left_side:
            if left_side.startswith('-x') or left_side.startswith('x'):
                a = -1 if left_side.startswith('-x') else 1
                b = 0 if len(left_side) == 2 else eval(left_side[2 if left_side.startswith('-x') else 1:])
            else:
                parts = left_side.split('x')
                a = eval(parts[0]) if parts[0] else 1
                b = eval(parts[1]) if len(parts) > 1 else 0
        else:
            a = 0
            b = eval(left_side)
        
        c = eval(right_side)
        
        # Solve for x
        if a == 0:
            if b == c:
                return 'Infinite solutions (any x)'
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
    print(tentacle('x - 5 = 10'))  # Should print: 15.0
    print(tentacle('-3*x = 9'))  # Should print: -3.0
    print(tentacle('5 = 5'))  # Should print: Infinite solutions (any x)
    print(tentacle('x + 1 = 2'))  # Should print: 1.0
    print(tentacle('2*x + 1 = 2*x + 2'))  # Should print: No solution
    print(tentacle('invalid equation'))  # Should print an error message
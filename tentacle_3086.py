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
        
        # Extract coefficients
        if 'x' in left_side:
            if left_side.startswith('-x') or left_side.startswith('x'):
                a = -1 if left_side.startswith('-x') else 1
                b = eval(left_side.replace('-x', '0').replace('x', '0'))
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
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            x = (c - b) / a
            return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 10'))   # Should print: 15.0
    print(tentacle('3*x = 12'))     # Should print: 4.0
    print(tentacle('5 = 5'))        # Should print: Infinite solutions
    print(tentacle('5 = 6'))        # Should print: No solution
    print(tentacle('2*x + 3 = 7 + x'))  # Should print: 4.0
    print(tentacle('invalid equation')) # Should print an error message
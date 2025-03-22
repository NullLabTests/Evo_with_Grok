# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x and return the value of x.

    Args:
    equation (str): A string containing a linear equation in the form 'ax + b = c'.

    Returns:
    str: The solution for x as a string.

    Example:
    >>> tentacle('2*x + 3 = 7')
    '2'
    """
    try:
        # Remove spaces and split the equation at the equals sign
        equation = equation.replace(" ", "").split("=")
        
        # Parse left and right sides of the equation
        left_side = equation[0]
        right_side = equation[1]
        
        # Extract coefficients of x and constant term from left side
        if 'x' in left_side:
            if left_side.startswith('x'):
                a = 1 if left_side == 'x' else eval(left_side[0])
            elif left_side.endswith('x'):
                a = eval(left_side[:-1])
            else:
                a = eval(left_side.split('x')[0])
        else:
            a = 0
        
        # Extract constant term from left side
        b = eval(left_side.replace('x', '0')) if 'x' in left_side else eval(left_side)
        
        # Evaluate right side
        c = eval(right_side)
        
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
    print(tentacle('3*x = 12'))  # Should print: 4.0
    print(tentacle('0*x + 2 = 2'))  # Should print: All real numbers
    print(tentacle('0*x + 2 = 3'))  # Should print: No solution
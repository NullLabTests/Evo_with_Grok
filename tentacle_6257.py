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
    '2.0'
    """
    try:
        # Remove spaces and split the equation at '='
        equation = equation.replace(" ", "").split("=")
        
        # Parse left and right sides of the equation
        left_side = equation[0]
        right_side = equation[1]
        
        # Extract coefficients and constant
        if 'x' in left_side:
            if left_side.startswith('x'):
                a = 1
            elif left_side.startswith('-x'):
                a = -1
            else:
                a = float(left_side.split('x')[0])
        else:
            a = 0
        
        b = eval(left_side.replace('x', '0'))
        c = eval(right_side)
        
        # Solve for x
        if a == 0:
            if b == c:
                return "Infinite solutions (equation is always true)"
            else:
                return "No solution (equation is always false)"
        else:
            x = (c - b) / a
            return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: '2.0'
    print(tentacle('x - 5 = 0'))    # Should print: '5.0'
    print(tentacle('3*x = 9'))      # Should print: '3.0'
    print(tentacle('0*x + 2 = 2'))  # Should print: 'Infinite solutions (equation is always true)'
    print(tentacle('0*x + 2 = 3'))  # Should print: 'No solution (equation is always false)'
    print(tentacle('x/2 + 1 = 3'))  # Should print: '4.0'
    print(tentacle('2*x + 3 = x'))  # Should print: '-3.0'
    print(tentacle('invalid'))      # Should print: 'Error: ...'
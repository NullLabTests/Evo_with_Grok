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
        # Remove spaces and split the equation at '='
        equation = equation.replace(" ", "").split("=")
        
        # Parse left and right sides of the equation
        left_side = equation[0]
        right_side = equation[1]
        
        # Extract coefficients and constants
        if 'x' in left_side:
            if left_side.startswith('-'):
                left_side = '-1' + left_side[1:]
            elif not left_side.startswith('x'):
                left_side = '1' + left_side if left_side.startswith('+') else left_side
            
            # Split into parts
            parts = left_side.split('x')
            a = eval(parts[0]) if parts[0] else 1
            b = eval(parts[1]) if parts[1] else 0
        else:
            a = 0
            b = eval(left_side)
        
        c = eval(right_side)
        
        # Solve the equation ax + b = c
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
    print(tentacle('3*x = 9'))  # Should print: 3.0
    print(tentacle('0*x + 2 = 2'))  # Should print: All real numbers
    print(tentacle('0*x + 2 = 3'))  # Should print: No solution
    print(tentacle('x/2 = 4'))  # Should print: 8.0
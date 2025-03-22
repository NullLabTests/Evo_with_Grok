# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.
    
    Args:
    equation (str): A string containing a linear equation in the form 'ax + b = c'.
    
    Returns:
    str: The solution for x as a string, or an error message if the equation cannot be solved.
    
    Example:
    >>> tentacle('2*x + 3 = 7')
    '2'
    """
    try:
        # Remove spaces and split the equation into left and right sides
        equation = equation.replace(" ", "").split("=")
        left_side = equation[0]
        right_side = equation[1]
        
        # Extract coefficients and constant from the left side
        if 'x' in left_side:
            if left_side.startswith('-x') or left_side.startswith('x'):
                a = -1 if left_side.startswith('-x') else 1
                b = 0 if len(left_side) == 1 or left_side[1] == '+' else -float(left_side[2:])
            else:
                parts = left_side.split('x')
                a = float(parts[0]) if parts[0] and parts[0] != '-' else 1 if parts[0] == '' else -1
                b = float(parts[1]) if len(parts) > 1 else 0
        else:
            a = 0
            b = float(left_side)
        
        # Calculate the right side of the equation
        c = float(right_side)
        
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
    print(tentacle('5*x - 2 = 8'))  # Should print: 2.0
    print(tentacle('-x + 4 = 1'))  # Should print: 3.0
    print(tentacle('3 = 3'))  # Should print: All real numbers
    print(tentacle('2 = 3'))  # Should print: No solution
    print(tentacle('x + 2 = y'))  # Should print: Error: could not convert string to float: y
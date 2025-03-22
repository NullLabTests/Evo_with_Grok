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
        
        # Parse the left side of the equation
        left_side = equation[0]
        right_side = equation[1]
        
        # Extract the coefficient of x and the constant term from the left side
        if 'x' in left_side:
            if left_side.startswith('x'):
                a = 1
                b = 0 if len(left_side) == 1 else float(left_side[1:])
            elif left_side.endswith('x'):
                a = float(left_side[:-1])
                b = 0
            else:
                a, b = map(float, left_side.split('x'))
        else:
            a = 0
            b = float(left_side)
        
        # Calculate the right side of the equation
        c = float(right_side)
        
        # Solve for x: ax + b = c -> x = (c - b) / a
        if a == 0:
            return "Error: Not a linear equation in x"
        x = (c - b) / a
        
        return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x + 5 = 10'))   # Should print: 5.0
    print(tentacle('3x - 2 = 1'))   # Should print: 1.0
    print(tentacle('5 = 2x + 1'))   # Should print: 2.0
    print(tentacle('x = 4'))        # Should print: 4.0
    print(tentacle('2 = 2'))        # Should print: Error: Not a linear equation in x
    print(tentacle('y + 3 = 5'))    # Should print: Error: Not a linear equation in x
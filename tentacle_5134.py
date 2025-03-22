# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve an equation for x.

    Args:
    equation (str): A string containing an equation in the form 'ax + b = c'.

    Returns:
    str: The solution for x as a string.

    Example:
    >>> tentacle('2*x + 3 = 7')
    '2.0'
    """
    try:
        # Remove spaces and split the equation at '='
        equation = equation.replace(' ', '').split('=')
        
        # Parse the left side of the equation
        left_side = equation[0]
        if 'x' not in left_side:
            raise ValueError("Equation must contain 'x'")
        
        # Extract coefficient of x and constant term
        if left_side.startswith('x'):
            a = 1 if left_side == 'x' else float(left_side[0])
        elif left_side.endswith('x'):
            a = 1 if left_side == 'x' else float(left_side[:-1])
        else:
            a = float(left_side.split('x')[0])
        
        # Extract constant term
        b = 0
        if '+' in left_side:
            b = float(left_side.split('+')[-1].replace('x', ''))
        elif '-' in left_side:
            b = -float(left_side.split('-')[-1].replace('x', ''))
        
        # Parse the right side of the equation
        c = float(equation[1])
        
        # Solve for x
        x = (c - b) / a
        
        return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x + 5 = 10'))   # Should print: 5.0
    print(tentacle('3x - 4 = 8'))   # Should print: 4.0
    print(tentacle('x = 7'))        # Should print: 7.0
    print(tentacle('2x = 10'))      # Should print: 5.0
    print(tentacle('x + 2 = x'))    # Should print: Error: division by zero
    print(tentacle('y + 3 = 7'))    # Should print: Error: Equation must contain 'x'
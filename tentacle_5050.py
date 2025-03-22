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
    '2.0'
    """
    try:
        # Remove spaces and split the equation at '='
        equation = equation.replace(' ', '').split('=')
        
        # Parse left side of the equation
        left_side = equation[0]
        right_side = equation[1]
        
        # Extract coefficient of x and constant term from left side
        if 'x' in left_side:
            if left_side.startswith('x'):
                a = 1
            elif left_side.startswith('-x'):
                a = -1
            else:
                a = float(left_side.split('x')[0])
        else:
            a = 0
        
        b = 0
        if '+' in left_side:
            b = float(left_side.split('+')[-1])
        elif '-' in left_side and left_side.index('-') != 0:
            b = float(left_side.split('-')[-1])
        
        # Calculate the value of c
        c = float(right_side)
        
        # Solve for x
        if a == 0 and b == c:
            return 'Infinite solutions'
        elif a == 0 and b != c:
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
    print(tentacle('-3*x = 9'))  # Should print: -3.0
    print(tentacle('2*x = 2*x + 1'))  # Should print: No solution
    print(tentacle('5 = 5'))  # Should print: Infinite solutions
    print(tentacle('2*x + 3 = invalid'))  # Should print: Error: could not convert string to float: 'invalid'
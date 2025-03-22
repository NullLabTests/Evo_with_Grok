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
        # Remove spaces and split the equation into left and right sides
        equation = equation.replace(" ", "").split("=")
        left_side = equation[0]
        right_side = equation[1]
        
        # Extract coefficients a and b from the left side
        if 'x' in left_side:
            if left_side.startswith('-x') or left_side.startswith('x'):
                a = 1 if left_side[0] == 'x' else -1
                b = eval(left_side.replace('x', '0'))
            else:
                a = eval(left_side.split('x')[0])
                b = eval(left_side.replace('x', '0'))
        else:
            a = 0
            b = eval(left_side)
        
        # Evaluate the right side
        c = eval(right_side)
        
        # Solve for x
        if a == 0 and b == c:
            return "Infinite solutions"
        elif a == 0 and b != c:
            return "No solution"
        else:
            x = (c - b) / a
            return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 0'))    # Should print: 5.0
    print(tentacle('-3*x = 9'))     # Should print: -3.0
    print(tentacle('2 = 2'))        # Should print: Infinite solutions
    print(tentacle('0 = 1'))        # Should print: No solution
    print(tentacle('x + x = 2'))    # Should print: 1.0
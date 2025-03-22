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
        
        # Extract coefficients and constants
        if 'x' in left_side:
            if '*' in left_side:
                a, b = left_side.split('+')
                a = float(a.replace('x', '').replace('*', ''))
            else:
                if left_side.startswith('x'):
                    a = 1
                    b = float(left_side[1:]) if left_side[1:] else 0
                else:
                    a = float(left_side.split('x')[0])
                    b = float(left_side.split('x')[1]) if left_side.split('x')[1] else 0
        else:
            a = 0
            b = float(left_side)
        
        c = float(right_side)
        
        # Solve the equation ax + b = c
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
    print(tentacle('x + 5 = 10'))   # Should print: 5.0
    print(tentacle('3x - 2 = 10'))  # Should print: 4.0
    print(tentacle('x = 5'))        # Should print: 5.0
    print(tentacle('2 = 2'))        # Should print: Infinite solutions
    print(tentacle('2 = 3'))        # Should print: No solution
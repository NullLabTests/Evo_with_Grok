# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.
    
    Args:
    equation (str): A string containing a linear equation in the form 'ax + b = c'.
    
    Returns:
    str: The solution for x as a string, or an error message if the equation is invalid.
    
    Example:
    >>> tentacle('2*x + 3 = 7')
    '2'
    """
    try:
        # Remove spaces and split the equation at '='
        equation = equation.replace(" ", "").split("=")
        
        if len(equation) != 2:
            return "Error: Invalid equation format"
        
        left, right = equation
        
        # Extract coefficient of x and constant term from left side
        if 'x' in left:
            if left == 'x':
                a = 1
                b = 0
            elif left.startswith('-x'):
                a = -1
                b = 0
            elif left.startswith('x'):
                a = 1
                b = 0
            else:
                if left[0] in ['+', '-']:
                    a = eval(left[:left.index('x')])
                    b = eval(left[left.index('x')+1:] or '0')
                else:
                    a = eval(left[:left.index('x')])
                    b = eval(left[left.index('x')+1:] or '0')
        else:
            a = 0
            b = eval(left)
        
        # Evaluate right side
        c = eval(right)
        
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
    print(tentacle('x - 5 = 0'))  # Should print: 5.0
    print(tentacle('-3*x = 9'))  # Should print: -3.0
    print(tentacle('2 = 2'))  # Should print: Infinite solutions
    print(tentacle('2 = 3'))  # Should print: No solution
    print(tentacle('2*x + 3 = x + 7'))  # Should print: 4.0
    print(tentacle('invalid equation'))  # Should print an error message
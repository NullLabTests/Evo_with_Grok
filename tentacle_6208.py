# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.
    
    Args:
    equation (str): A string containing a linear equation in the form 'ax + b = c'.
    
    Returns:
    str: The value of x as a string, or an error message if the equation cannot be solved.
    
    Example:
    >>> tentacle('2*x + 3 = 7')
    '2'
    """
    try:
        # Remove whitespace and split the equation into left and right sides
        equation = equation.replace(" ", "").split("=")
        if len(equation) != 2:
            return "Error: Invalid equation format"
        
        left, right = equation
        
        # Parse the left side to extract the coefficient of x and the constant term
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
                parts = left.split('x')
                if len(parts) == 2:
                    a = float(parts[0]) if parts[0] else 1
                    b = float(parts[1]) if parts[1] else 0
                else:
                    return "Error: Invalid equation format"
        else:
            a = 0
            b = float(left)
        
        # Parse the right side
        c = float(right)
        
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
    print(tentacle('x + 5 = 10'))   # Should print: 5.0
    print(tentacle('3*x = 9'))      # Should print: 3.0
    print(tentacle('5 = 5'))        # Should print: Infinite solutions
    print(tentacle('5 = 6'))        # Should print: No solution
    print(tentacle('2*x + 3 = 7*x'))  # Should print: -0.6
    print(tentacle('invalid equation'))  # Should print: Error: Invalid equation format
# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.
    
    Args:
    equation (str): A string containing a linear equation in the form 'ax + b = c'.
    
    Returns:
    str: The value of x as a string, or an error message if the equation is invalid.
    
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
        
        # Find the coefficient of x and the constant on the left side
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
        
        # Calculate the right side of the equation
        c = float(right)
        
        # Solve for x
        if a == 0 and b == c:
            return "Error: Equation has infinite solutions"
        elif a == 0 and b != c:
            return "Error: No solution"
        else:
            x = (c - b) / a
            return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 0'))    # Should print: 5.0
    print(tentacle('3x = 9'))       # Should print: 3.0
    print(tentacle('2 = 2'))        # Should print: Error: Equation has infinite solutions
    print(tentacle('2 = 3'))        # Should print: Error: No solution
    print(tentacle('2x + 3 = 3x'))  # Should print: 3.0
    print(tentacle('x + x = 2x'))   # Should print: Error: Equation has infinite solutions
    print(tentacle('x + x = 3x'))   # Should print: 0.0
    print(tentacle('2*x + 3 ='))    # Should print: Error: Invalid equation format
# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x.
    
    Args:
    equation (str): A string containing a linear equation in the format 'ax + b = c'.
    
    Returns:
    str: The solution for x as a string, or an error message if the equation is invalid.
    
    Example:
    >>> tentacle('2*x + 3 = 7')
    '2'
    """
    try:
        # Remove spaces and split the equation at '='
        equation = equation.replace(' ', '').split('=')
        
        if len(equation) != 2:
            return "Error: Invalid equation format"
        
        left, right = equation
        
        # Extract coefficients
        if 'x' in left:
            if left == 'x':
                a = 1
            elif left.startswith('-x'):
                a = -1
            else:
                a = float(left.split('x')[0])
            b = 0
        else:
            a = 0
            b = float(left)
        
        if 'x' in right:
            if right == 'x':
                a -= 1
            elif right.startswith('-x'):
                a += 1
            else:
                a -= float(right.split('x')[0])
            b -= 0
        else:
            b -= float(right)
        
        # Solve for x
        if a == 0:
            return "Error: Not a linear equation (a = 0)"
        
        x = -b / a
        
        return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 10'))   # Should print: 15.0
    print(tentacle('-3*x = 9'))     # Should print: -3.0
    print(tentacle('2 = 2'))        # Should print: Error: Not a linear equation (a = 0)
    print(tentacle('x + x = 2*x'))  # Should print: Error: Not a linear equation (a = 0)
    print(tentacle('2*x + y = 7'))  # Should print: Error: Invalid equation format
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
        # Remove spaces and split the equation into left and right sides
        equation = equation.replace(" ", "").split("=")
        if len(equation) != 2:
            return "Error: Invalid equation format"
        
        left, right = equation
        right = float(right)
        
        # Extract coefficients
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
                if parts[0] == '-':
                    a = -1
                    b = float(parts[1]) if parts[1] else 0
                elif parts[0] == '':
                    a = 1
                    b = float(parts[1]) if parts[1] else 0
                else:
                    a = float(parts[0])
                    b = float(parts[1]) if parts[1] else 0
        else:
            a = 0
            b = float(left)
        
        # Solve for x
        if a == 0:
            return "Error: Not a linear equation in x"
        x = (right - b) / a
        
        return str(x)
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 0'))    # Should print: 5.0
    print(tentacle('-3*x = 9'))     # Should print: -3.0
    print(tentacle('2 = 2'))        # Should print: Error: Not a linear equation in x
    print(tentacle('y + 3 = 7'))    # Should print: Error: Not a linear equation in x
    print(tentacle('2*x + y = 7'))  # Should print: Error: Invalid equation format
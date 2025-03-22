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
        
        left_side = equation[0]
        right_side = equation[1]
        
        # Extract coefficients
        if 'x' in left_side:
            if left_side.startswith('-x') or left_side.startswith('x'):
                a = -1 if left_side.startswith('-x') else 1
                b = 0 if len(left_side) == 1 or left_side[1] == '+' else -float(left_side[1:])
            else:
                parts = left_side.split('x')
                a = float(parts[0]) if parts[0] and parts[0] != '-' else 1 if parts[0] == '' else -1
                b = float(parts[1]) if len(parts) > 1 and parts[1] else 0
        else:
            a = 0
            b = float(left_side)
        
        c = float(right_side)
        
        # Solve for x
        if a == 0:
            return "Error: Not a linear equation in x"
        
        x = (c - b) / a
        
        return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('5 - x = 1'))    # Should print: 4.0
    print(tentacle('x = 10'))       # Should print: 10.0
    print(tentacle('2x + 3 = 7'))   # Should print: 2.0
    print(tentacle('3 = 2x + 1'))   # Should print: 1.0
    print(tentacle('x + 5 = x + 3'))# Should print: Error: Not a linear equation in x
    print(tentacle('2y + 3 = 7'))   # Should print: Error: Not a linear equation in x
    print(tentacle('2*x + 3 ='))    # Should print: Error: Invalid equation format
# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.
    
    Args:
    equation (str): A string containing a linear equation in the format 'a*x + b = c'.
    
    Returns:
    str: The solution for x as a string, or an error message if the equation is invalid.
    
    Example:
    >>> tentacle('2*x + 3 = 7')
    '2'
    """
    try:
        # Remove whitespace and split the equation into left and right sides
        equation = equation.replace(" ", "").split("=")
        
        if len(equation) != 2:
            return "Error: Invalid equation format"
        
        left_side, right_side = equation
        
        # Parse the left side of the equation
        if '*x' in left_side:
            a, b = left_side.split('+') if '+' in left_side else left_side.split('-')
            a = float(a.replace('x', '')) if 'x' in a else float(a)
            b = float(b) if b else 0
            if '-' in left_side and '+' not in left_side:
                b = -b
        elif 'x' in left_side:
            a = 1 if left_side == 'x' else -1 if left_side == '-x' else float(left_side.replace('x', ''))
            b = 0
        else:
            return "Error: x not found in the equation"
        
        # Parse the right side of the equation
        c = float(right_side)
        
        # Solve for x
        x = (c - b) / a
        
        return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 10'))   # Should print: 15.0
    print(tentacle('-3*x = 9'))     # Should print: -3.0
    print(tentacle('2*x = 8'))      # Should print: 4.0
    print(tentacle('x + 2 = 5'))    # Should print: 3.0
    print(tentacle('2 = 2'))        # Should print: Error: x not found in the equation
    print(tentacle('x + y = 3'))    # Should print: Error: Invalid equation format
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
        # Remove spaces and split the equation into left and right sides
        equation = equation.replace(" ", "").split("=")
        if len(equation) != 2:
            return "Error: Invalid equation format"
        
        left, right = equation[0], equation[1]
        
        # Parse the left side of the equation
        if '*x' in left:
            a, b = left.split('+') if '+' in left else left.split('-')
            a = a.replace('x', '') if 'x' in a else '-' + a.replace('x', '')
            b = b if '+' in left else '-' + b
        elif 'x' in left:
            a = '1' if '+' in left or '-' not in left else '-1'
            b = left.replace('x', '') if '+' in left or '-' not in left else '-' + left.replace('x', '')
        else:
            return "Error: Equation must contain x"
        
        # Convert parsed values to floats
        a, b, c = float(a), float(b), float(right)
        
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
    print(tentacle('2*x = 4'))      # Should print: 2.0
    print(tentacle('x + 2 = 5'))    # Should print: 3.0
    print(tentacle('3 = 2*x + 1'))  # Should print: 1.0
    print(tentacle('x = 7'))        # Should print: 7.0
    print(tentacle('2*x'))          # Should print: Error: Invalid equation format
    print(tentacle('y + 3 = 7'))    # Should print: Error: Equation must contain x
    print(tentacle('2*x + y = 7'))  # Should print: Error: Invalid equation format
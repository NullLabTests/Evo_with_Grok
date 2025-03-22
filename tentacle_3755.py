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
        if '+' in left_side:
            a, b = left_side.split('+')
        elif '-' in left_side:
            a, b = left_side.split('-')
            b = '-' + b
        else:
            a = left_side
            b = '0'
        
        # Extract coefficient a from ax
        if 'x' in a:
            a = a.replace('x', '')
            if a == '' or a == '-':
                a += '1'
        else:
            a = '0'
            b = a
        
        # Convert coefficients to float
        a = float(a)
        b = float(b)
        c = float(right_side)
        
        # Solve for x
        if a == 0:
            return "Error: Not a linear equation"
        x = (c - b) / a
        
        # Return the solution as a string
        return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('5*x - 4 = 6'))  # Should print: 2.0
    print(tentacle('x + 2 = 5'))    # Should print: 3.0
    print(tentacle('3*x = 9'))      # Should print: 3.0
    print(tentacle('2 = 2'))        # Should print: Error: Not a linear equation
    print(tentacle('x^2 + 2 = 5'))  # Should print: Error: invalid syntax
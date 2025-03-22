# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x.

    Args:
    equation (str): A string containing a linear equation in the form 'ax + b = c'.

    Returns:
    str: The solution for x as a string.

    Example:
    >>> tentacle('2*x + 3 = 7')
    '2'
    """
    try:
        # Remove spaces and split the equation at '='
        equation = equation.replace(" ", "").split("=")
        
        # Parse left and right sides of the equation
        left_side = equation[0]
        right_side = equation[1]
        
        # Extract coefficients and constants
        if 'x' in left_side:
            if '+' in left_side or '-' in left_side:
                a, b = left_side.split('x')
                a = a if a else '1'
                a = a if a != '-' else '-1'
                b = b if b else '0'
            else:
                a = left_side.replace('x', '') if left_side != 'x' else '1'
                b = '0'
        else:
            a = '0'
            b = left_side
        
        c = right_side
        
        # Convert strings to floats
        a = float(eval(a))
        b = float(eval(b))
        c = float(eval(c))
        
        # Solve for x
        if a == 0:
            return "Error: Not a linear equation in x"
        x = (c - b) / a
        
        # Return the solution as a string
        return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('5*x - 2 = 8'))  # Should print: 2.0
    print(tentacle('-x + 4 = 1'))   # Should print: 3.0
    print(tentacle('x = 5'))        # Should print: 5.0
    print(tentacle('2*x = 6'))      # Should print: 3.0
    print(tentacle('3 = 3'))        # Should print: Error: Not a linear equation in x
    print(tentacle('y + 2 = 4'))    # Should print: Error: Not a linear equation in x
    print(tentacle('2*x + y = 5'))  # Should print: Error: Not a linear equation in x
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
        
        # Evaluate the right side of the equation
        c = eval(right_side)
        
        # Extract the coefficient of x and the constant term from the left side
        if '+' in left_side:
            a, b = left_side.split('+')
        elif '-' in left_side:
            a, b = left_side.split('-')
            b = '-' + b
        else:
            a = left_side
            b = '0'
        
        # Extract the coefficient of x
        if a == 'x':
            a = '1'
        elif a == '-x':
            a = '-1'
        elif 'x' in a:
            a = a.replace('x', '')
        
        # Evaluate a and b
        a = eval(a)
        b = eval(b)
        
        # Solve for x
        x = (c - b) / a
        
        # Return the solution as a string
        return str(x)
    
    except Exception as e:
        # Return an error message if solving fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 10'))   # Should print: 15.0
    print(tentacle('-3*x = 9'))     # Should print: -3.0
    print(tentacle('x/2 = 4'))      # Should print: 8.0
    print(tentacle('2*x + 3 = y'))  # Should print: Error: name 'y' is not defined
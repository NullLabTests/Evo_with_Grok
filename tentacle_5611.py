# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.
    
    Args:
    equation (str): A string containing a linear equation in the form 'ax + b = c'.
    
    Returns:
    str: The solution for x as a string, or an error message if solving fails.
    
    Example:
    >>> tentacle('2*x + 3 = 7')
    '2.0'
    """
    try:
        # Remove spaces and split the equation into left and right sides
        equation = equation.replace(" ", "").split("=")
        left_side = equation[0]
        right_side = equation[1]
        
        # Isolate the x term on the left side
        if '+' in left_side:
            left_side = left_side.split('+')
            constant = float(left_side[1])
            x_term = left_side[0]
        elif '-' in left_side:
            left_side = left_side.split('-')
            constant = -float(left_side[1])
            x_term = left_side[0]
        else:
            constant = 0
            x_term = left_side
        
        # Extract coefficient of x
        if '*' in x_term:
            coefficient = float(x_term.split('*')[0])
        else:
            coefficient = 1
        
        # Calculate the value of x
        right_value = float(right_side)
        x = (right_value - constant) / coefficient
        
        return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 10'))   # Should print: 15.0
    print(tentacle('3*x = 12'))     # Should print: 4.0
    print(tentacle('x + 2 = 0'))    # Should print: -2.0
    print(tentacle('2*x - 3 = 7'))  # Should print: 5.0
    print(tentacle('invalid'))      # Should print an error message
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
        
        # Isolate the x term on the left side
        if '+' in left_side:
            left_side = left_side.split('+')
            constant = left_side[1]
            x_term = left_side[0]
        elif '-' in left_side:
            left_side = left_side.split('-')
            constant = '-' + left_side[1]
            x_term = left_side[0]
        else:
            x_term = left_side
            constant = '0'
        
        # Extract coefficient of x
        if 'x' in x_term:
            if x_term == 'x':
                coefficient = '1'
            elif x_term == '-x':
                coefficient = '-1'
            else:
                coefficient = x_term.replace('x', '')
        else:
            raise ValueError("Equation must contain 'x'")
        
        # Solve for x
        x = (float(right_side) - float(constant)) / float(coefficient)
        
        return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('5*x - 2 = 8'))  # Should print: 2.0
    print(tentacle('x + 4 = 10'))   # Should print: 6.0
    print(tentacle('-3*x = 9'))     # Should print: -3.0
    print(tentacle('2*x = 0'))      # Should print: 0.0
    print(tentacle('x = 5'))        # Should print: 5.0
    print(tentacle('2*y + 3 = 7'))  # Should print: Error: Equation must contain 'x'
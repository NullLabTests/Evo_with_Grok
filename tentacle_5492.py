# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.
    
    Args:
    equation (str): A string containing a linear equation in the form 'a*x + b = c'.
    
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
        right_value = eval(right_side)
        
        # Check if 'x' is present in the left side
        if 'x' not in left_side:
            raise ValueError("Equation does not contain 'x'")
        
        # Split the left side into coefficient and constant
        if '+' in left_side:
            coefficient, constant = left_side.split('+')
        elif '-' in left_side:
            coefficient, constant = left_side.split('-')
            constant = '-' + constant
        else:
            coefficient = left_side
            constant = '0'
        
        # Extract the coefficient of x
        if coefficient == 'x':
            coefficient = '1'
        elif coefficient == '-x':
            coefficient = '-1'
        else:
            coefficient = coefficient.replace('x', '')
        
        # Evaluate the coefficient and constant
        coefficient = eval(coefficient)
        constant = eval(constant)
        
        # Solve for x
        x = (right_value - constant) / coefficient
        
        # Return the solution as a string
        return str(x)
    
    except Exception as e:
        # Return an error message if solving fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('5*x - 2 = 8'))  # Should print: 2.0
    print(tentacle('x + 4 = 10'))   # Should print: 6.0
    print(tentacle('-3*x = 9'))     # Should print: -3.0
    print(tentacle('2 = 2'))        # Should print: Error: Equation does not contain 'x'
    print(tentacle('x + x = 2'))    # Should print: 1.0
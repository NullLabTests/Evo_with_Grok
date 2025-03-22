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
    '2'
    """
    try:
        # Remove spaces and split the equation at '='
        equation = equation.replace(" ", "").split("=")
        
        # Parse left and right sides of the equation
        left_side = equation[0]
        right_side = equation[1]
        
        # Extract the coefficient of x and the constant term from the left side
        if '+' in left_side:
            coefficient, constant = left_side.split('+')
        elif '-' in left_side:
            coefficient, constant = left_side.split('-')
            constant = '-' + constant
        else:
            coefficient = left_side
            constant = '0'
        
        # Extract x from the coefficient
        if 'x' in coefficient:
            if coefficient == 'x':
                coefficient = '1'
            elif coefficient == '-x':
                coefficient = '-1'
            else:
                coefficient = coefficient.replace('x', '')
        else:
            coefficient = '0'
        
        # Convert all parts to floats
        coefficient = float(coefficient)
        constant = float(constant)
        right_side = float(right_side)
        
        # Solve for x
        if coefficient == 0:
            return "Error: Division by zero"
        x = (right_side - constant) / coefficient
        
        # Return the solution as a string
        return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 10'))   # Should print: 15.0
    print(tentacle('3*x = 9'))      # Should print: 3.0
    print(tentacle('x + 2 = 2'))    # Should print: 0.0
    print(tentacle('2 = 2'))        # Should print: Error: Division by zero
    print(tentacle('x + y = 5'))    # Should print: Error: name 'y' is not defined
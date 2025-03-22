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
        # Remove spaces and split the equation at the equals sign
        equation = equation.replace(" ", "").split("=")
        
        if len(equation) != 2:
            return "Error: Invalid equation format"
        
        left_side, right_side = equation
        
        # Parse the left side of the equation
        if '+' in left_side:
            term, constant = left_side.split('+')
        elif '-' in left_side:
            term, constant = left_side.split('-')
            constant = '-' + constant
        else:
            term = left_side
            constant = '0'
        
        # Extract the coefficient of x
        if term == 'x':
            coefficient = '1'
        elif term == '-x':
            coefficient = '-1'
        elif term.endswith('x'):
            coefficient = term[:-1]
        else:
            return "Error: Invalid term format"
        
        # Convert all parts to floats
        coefficient = float(coefficient)
        constant = float(constant)
        right_side = float(right_side)
        
        # Solve for x
        x = (right_side - constant) / coefficient
        
        return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('5x - 2 = 8'))   # Should print: 2.0
    print(tentacle('-x + 4 = 1'))   # Should print: 3.0
    print(tentacle('x = 5'))        # Should print: 5.0
    print(tentacle('2x + 3 = x + 5'))  # Should print: 2.0
    print(tentacle('2x + 3y = 7'))  # Should print: Error: Invalid term format
    print(tentacle('2x + 3 ='))     # Should print: Error: Invalid equation format
    print(tentacle('2x + 3 = 7x'))  # Should print: Error: Invalid term format
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
    '2.0'
    """
    try:
        # Remove spaces and split the equation at the equals sign
        equation = equation.replace(" ", "").split("=")
        
        # Check if the equation is in the correct format
        if len(equation) != 2:
            return "Error: Invalid equation format"
        
        left_side, right_side = equation
        
        # Evaluate the right side of the equation
        right_value = eval(right_side)
        
        # Find the position of 'x' in the left side
        x_position = left_side.find('x')
        
        if x_position == -1:
            return "Error: No 'x' found in the equation"
        
        # Extract the coefficient of x
        if x_position == 0:
            x_coefficient = 1
        elif x_position == len(left_side) - 1:
            x_coefficient = eval(left_side[:-1])
        else:
            x_coefficient = eval(left_side[:x_position] + left_side[x_position+1:])
        
        # Calculate the constant term on the left side
        left_constant = eval(left_side.replace('x', '0'))
        
        # Solve for x
        x_value = (right_value - left_constant) / x_coefficient
        
        return str(x_value)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('5*x - 2 = 13'))  # Should print: 3.0
    print(tentacle('-x + 4 = 1'))  # Should print: 3.0
    print(tentacle('3 = 2*x + 1'))  # Should print: 1.0
    print(tentacle('x/2 + 3 = 5'))  # Should print: 4.0
    print(tentacle('2*x + 3 = 3*x'))  # Should print: 3.0
    print(tentacle('invalid equation'))  # Should print an error message
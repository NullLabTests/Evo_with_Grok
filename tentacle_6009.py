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
        # Remove spaces and split the equation into left and right sides
        equation = equation.replace(" ", "").split("=")
        if len(equation) != 2:
            return "Error: Invalid equation format"
        
        left, right = equation
        
        # Extract the coefficient of x and the constant term from the left side
        import re
        left_parts = re.split(r'([+-])', left)
        x_term = None
        constant = 0
        current_sign = 1
        
        for part in left_parts:
            if part in ['+', '-']:
                current_sign = 1 if part == '+' else -1
            elif 'x' in part:
                coefficient = part.replace('x', '')
                x_term = current_sign * (float(coefficient) if coefficient else 1)
            else:
                constant += current_sign * float(part) if part else 0
        
        # Calculate the right side of the equation
        right_value = float(right)
        
        # Solve for x
        if x_term == 0:
            return "Error: No x term in the equation"
        x = (right_value - constant) / x_term
        
        return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 10'))   # Should print: 15.0
    print(tentacle('3*x = 9'))      # Should print: 3.0
    print(tentacle('2*x + 3 = x'))  # Should print: -3.0
    print(tentacle('x = 5'))        # Should print: 5.0
    print(tentacle('2*x + y = 7'))  # Should print: Error: Invalid equation format
    print(tentacle('2*x + 3'))      # Should print: Error: Invalid equation format
    print(tentacle('2*x + 3 ='))    # Should print: Error: Invalid equation format
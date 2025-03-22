# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.

    Args:
    equation (str): A string containing a linear equation in the format 'a*x + b = c'.

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

        left_side, right_side = equation[0], equation[1]
        
        # Parse the left side of the equation
        if 'x' not in left_side:
            return "Error: Equation must contain 'x'"
        
        # Split the left side into coefficient and constant parts
        parts = left_side.split('+')
        x_term = None
        constant = 0
        for part in parts:
            if 'x' in part:
                if x_term is not None:
                    return "Error: Multiple x terms detected"
                x_term = part.replace('x', '')
                if x_term == '':
                    x_term = '1'
                elif x_term == '-':
                    x_term = '-1'
                x_term = float(x_term)
            else:
                constant += float(part)
        
        if x_term is None:
            return "Error: No x term found"
        
        # Solve for x
        right_value = float(right_side)
        x = (right_value - constant) / x_term
        
        return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 10'))  # Should print: 15.0
    print(tentacle('-3*x + 2 = -4'))  # Should print: 2.0
    print(tentacle('2*x = 6'))  # Should print: 3.0
    print(tentacle('x + 1 = 1'))  # Should print: 0.0
    print(tentacle('2*x + 3 = 3*x'))  # Should print: 3.0
    print(tentacle('x = 5'))  # Should print: 5.0
    print(tentacle('2*x + y = 7'))  # Should print: Error: Equation must contain 'x'
    print(tentacle('2*x + 3 ='))  # Should print: Error: Invalid equation format
    print(tentacle('2*x + 3 = 7 = 8'))  # Should print: Error: Invalid equation format
    print(tentacle('2*x + 3*x = 7'))  # Should print: Error: Multiple x terms detected
    print(tentacle('2*x + 3 = y'))  # Should print: Error: could not convert string to float: 'y'
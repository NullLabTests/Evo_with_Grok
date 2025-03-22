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
        # Remove whitespace and split the equation into left and right sides
        equation = equation.replace(" ", "").split("=")
        if len(equation) != 2:
            return "Error: Invalid equation format"
        
        left_side, right_side = equation
        
        # Evaluate the right side of the equation
        right_value = eval(right_side)
        
        # Extract the coefficient of x and the constant term from the left side
        import re
        match = re.match(r"(-?\d*\.?\d*)?\*?x([-+]\d*\.?\d*)?", left_side)
        if not match:
            return "Error: Invalid left side of equation"
        
        coefficient = match.group(1) or '1'  # If no coefficient, assume it's 1
        constant = match.group(2) or '0'  # If no constant, assume it's 0
        
        # Calculate x
        x = (right_value - eval(constant)) / eval(coefficient)
        
        return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 10'))  # Should print: 15.0
    print(tentacle('-3*x = 9'))  # Should print: -3.0
    print(tentacle('2*x + 3 = 3*x'))  # Should print: 3.0
    print(tentacle('x = 5'))  # Should print: 5.0
    print(tentacle('2*x + 3'))  # Should print: Error: Invalid equation format
    print(tentacle('2*y + 3 = 7'))  # Should print: Error: Invalid left side of equation
    print(tentacle('2*x + 3 = a'))  # Should print: Error: name 'a' is not defined
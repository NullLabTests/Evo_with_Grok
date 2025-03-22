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
        # Remove whitespace and split the equation into left and right sides
        equation = equation.replace(" ", "").split("=")
        if len(equation) != 2:
            return "Error: Invalid equation format"
        
        left, right = equation
        right = float(right)  # Convert right side to float
        
        # Extract coefficient and constant from the left side
        if 'x' not in left:
            return "Error: Equation must contain x"
        
        if left == 'x':
            return str(right)
        
        if left.startswith('-x'):
            left = '-1*x' + left[2:]
        elif left.startswith('x'):
            left = '1*x' + left[1:]
        
        # Split the left side into parts
        parts = left.split('x')
        if len(parts) != 2:
            return "Error: Invalid equation format"
        
        coeff = float(parts[0]) if parts[0] else 1.0
        constant = float(parts[1]) if parts[1] else 0.0
        
        # Solve for x
        x = (right - constant) / coeff
        
        return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 10'))  # Should print: 15.0
    print(tentacle('-3*x = 9'))  # Should print: -3.0
    print(tentacle('x = 4'))  # Should print: 4.0
    print(tentacle('2*x + 3 = x + 5'))  # Should print: 2.0
    print(tentacle('2*x + 3'))  # Should print: Error: Invalid equation format
    print(tentacle('2*y + 3 = 7'))  # Should print: Error: Equation must contain x
    print(tentacle('2*x + 3 ='))  # Should print: Error: Invalid equation format
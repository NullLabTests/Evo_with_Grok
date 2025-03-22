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
        # Remove spaces and split the equation into left and right sides
        equation = equation.replace(" ", "").split("=")
        left_side = equation[0]
        right_side = equation[1]
        
        # Extract the coefficient of x and the constant term from the left side
        if 'x' in left_side:
            if left_side.startswith('-x') or left_side.startswith('x'):
                x_term = left_side[:2] if left_side.startswith('-x') else left_side[0]
                constant_term = left_side[2:] if left_side.startswith('-x') else left_side[1:]
            else:
                x_term = left_side.split('x')[0]
                constant_term = left_side.split('x')[1]
        else:
            x_term = '0'
            constant_term = left_side
        
        # Convert terms to floats
        a = float(x_term) if x_term else 1.0  # Default to 1 if no coefficient is specified
        b = float(constant_term) if constant_term else 0.0
        c = float(right_side)
        
        # Solve for x
        x = (c - b) / a
        
        # Return the solution rounded to 2 decimal places
        return f"{x:.2f}"
    
    except Exception as e:
        # Return an error message if solving fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.00
    print(tentacle('x - 5 = 10'))   # Should print: 15.00
    print(tentacle('-3*x = 9'))     # Should print: -3.00
    print(tentacle('x = 4'))        # Should print: 4.00
    print(tentacle('2*x + 3 = x'))  # Should print: -3.00
    print(tentacle('invalid'))      # Should print an error message
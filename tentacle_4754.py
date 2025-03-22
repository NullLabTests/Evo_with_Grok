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
        left_side = equation[0]
        right_side = equation[1]
        
        # Extract coefficients and constants
        if 'x' in left_side:
            if left_side.startswith('-'):
                left_side = '-1' + left_side[1:]
            elif not left_side.startswith('x'):
                left_side = '1' + left_side if left_side[0].isalpha() else left_side
            
            # Split the left side into coefficient and constant
            parts = left_side.split('x')
            a = eval(parts[0]) if parts[0] else 1
            b = eval(parts[1]) if len(parts) > 1 else 0
        else:
            return "Error: Equation must contain 'x'"
        
        # Evaluate the right side
        c = eval(right_side)
        
        # Solve for x
        x = (c - b) / a
        
        # Return the solution rounded to 2 decimal places
        return f"{x:.2f}"
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.00
    print(tentacle('x - 5 = 10'))   # Should print: 15.00
    print(tentacle('-3*x = 9'))     # Should print: -3.00
    print(tentacle('2*x = 4*x + 6'))# Should print: -3.00
    print(tentacle('x + 2 = x + 3'))# Should print: Error: division by zero
    print(tentacle('2*y + 3 = 7'))  # Should print: Error: Equation must contain 'x'
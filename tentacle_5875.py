# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.
    
    Args:
    equation (str): A string containing a linear equation in the form 'ax + b = c'.
    
    Returns:
    str: The solution for x as a string.
    
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
        
        # Extract coefficients of x and constant term from left side
        if '+' in left_side:
            terms = left_side.split('+')
            a = float(terms[0].replace('x', '1') if 'x' in terms[0] else terms[0])
            b = float(terms[1]) if len(terms) > 1 else 0
        elif '-' in left_side:
            terms = left_side.split('-')
            a = float(terms[0].replace('x', '1') if 'x' in terms[0] else terms[0])
            b = -float(terms[1]) if len(terms) > 1 else 0
        else:
            a = float(left_side.replace('x', '1') if 'x' in left_side else left_side)
            b = 0
        
        # Calculate c from the right side
        c = float(right_side)
        
        # Solve for x: ax + b = c -> x = (c - b) / a
        x = (c - b) / a
        
        # Return the solution rounded to 2 decimal places
        return f"{x:.2f}"
    
    except Exception as e:
        # Return an error message if solving fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.00
    print(tentacle('5*x - 4 = 6'))  # Should print: 2.00
    print(tentacle('-3*x = 9'))     # Should print: -3.00
    print(tentacle('x + 2 = 5'))    # Should print: 3.00
    print(tentacle('2*x = 10'))     # Should print: 5.00
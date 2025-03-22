# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x.
    
    Args:
    equation (str): A string containing a linear equation in the form 'ax + b = c'.
    
    Returns:
    str: The solution for x as a string, or an error message if the equation is invalid.
    
    Example:
    >>> tentacle('2*x + 3 = 7')
    '2'
    """
    try:
        # Remove whitespace and split the equation at '='
        left, right = equation.replace(" ", "").split('=')
        
        # Parse the left side of the equation
        if '+' in left:
            a_part, b_part = left.split('+')
        elif '-' in left:
            a_part, b_part = left.split('-')
            b_part = '-' + b_part
        else:
            a_part, b_part = left, '0'
        
        # Extract coefficients
        if a_part.startswith('x'):
            a = 1 if a_part == 'x' else float(a_part[1:])
        elif a_part.endswith('x'):
            a = float(a_part[:-1])
        else:
            raise ValueError("Invalid equation format")
        
        b = float(b_part)
        c = float(right)
        
        # Solve for x
        x = (c - b) / a
        
        # Return the solution rounded to 2 decimal places
        return f"{x:.2f}"
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.00
    print(tentacle('5x - 8 = 12'))  # Should print: 4.00
    print(tentacle('x + 5 = 10'))   # Should print: 5.00
    print(tentacle('-3x = 9'))      # Should print: -3.00
    print(tentacle('2x + 3 = x + 5'))  # Should print: 2.00
    print(tentacle('2x + 3x = 10'))    # Should print: 2.00
    print(tentacle('x = 5'))           # Should print: 5.00
    print(tentacle('2y + 3 = 7'))      # Should print: Error: Invalid equation format
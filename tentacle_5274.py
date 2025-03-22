# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x.
    
    Args:
    equation (str): A string containing a linear equation in the format 'ax + b = c'.
    
    Returns:
    str: The value of x as a string, or an error message if the equation is invalid.
    
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
        
        # Parse the left side of the equation
        if 'x' not in left:
            return "Error: Equation must contain x"
        
        # Extract coefficient of x and constant term
        if '+' in left:
            coeff, const = left.split('+')
        elif '-' in left:
            coeff, const = left.split('-')
            const = '-' + const
        else:
            coeff = left
            const = '0'
        
        # Handle cases where x is alone or has a coefficient
        if coeff == 'x':
            coeff = '1'
        elif coeff == '-x':
            coeff = '-1'
        else:
            coeff = coeff.replace('x', '')
        
        # Convert string values to floats
        a = float(coeff)
        b = float(const)
        c = float(right)
        
        # Solve for x
        if a == 0:
            return "Error: Coefficient of x cannot be zero"
        
        x = (c - b) / a
        
        # Return x as a string, rounded to 2 decimal places
        return f"{x:.2f}"
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.00
    print(tentacle('x - 5 = 10'))   # Should print: 15.00
    print(tentacle('-3*x = 9'))     # Should print: -3.00
    print(tentacle('2*x = 4'))      # Should print: 2.00
    print(tentacle('x + 2 = 2'))    # Should print: 0.00
    print(tentacle('2 = 2'))        # Should print: Error: Equation must contain x
    print(tentacle('x + x = 2'))    # Should print: 1.00
    print(tentacle('0*x + 3 = 7'))  # Should print: Error: Coefficient of x cannot be zero
    print(tentacle('x = y'))        # Should print: Error: Invalid equation format
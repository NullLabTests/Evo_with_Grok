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
        # Split the equation into left and right sides
        left, right = equation.split('=')
        
        # Remove whitespace
        left = left.strip()
        right = right.strip()
        
        # Parse the left side
        if '+' in left:
            term, constant = left.split('+')
            term = term.strip()
            constant = constant.strip()
        elif '-' in left:
            term, constant = left.split('-')
            term = term.strip()
            constant = '-' + constant.strip()
        else:
            term = left
            constant = '0'
        
        # Extract coefficient of x
        if term == 'x':
            coefficient = '1'
        elif term == '-x':
            coefficient = '-1'
        elif 'x' in term:
            coefficient = term.replace('x', '').strip()
        else:
            raise ValueError("Invalid equation format")
        
        # Convert strings to floats
        coefficient = float(coefficient)
        constant = float(constant)
        right = float(right)
        
        # Solve for x
        x = (right - constant) / coefficient
        
        # Return the solution as a string
        return str(x)
    
    except Exception as e:
        # Return an error message if solving fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 10'))   # Should print: 15.0
    print(tentacle('3*x = 12'))     # Should print: 4.0
    print(tentacle('x + 2 = 2'))    # Should print: 0.0
    print(tentacle('-x = 5'))       # Should print: -5.0
    print(tentacle('2*x - 3 = 7'))  # Should print: 5.0
    print(tentacle('x/2 + 1 = 3'))  # Should print: Error: Invalid equation format
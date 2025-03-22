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
        # Remove whitespace and split the equation at '='
        equation = equation.replace(" ", "").split("=")
        
        if len(equation) != 2:
            return "Error: Invalid equation format"
        
        left, right = equation
        
        # Isolate the x term on the left side
        if 'x' in right:
            left, right = right, left
        
        # Parse the left side
        if '+' in left:
            term, constant = left.split('+')
        elif '-' in left:
            term, constant = left.split('-')
            constant = '-' + constant
        else:
            term = left
            constant = '0'
        
        # Extract coefficient of x
        if term == 'x':
            a = 1
        elif term == '-x':
            a = -1
        elif term.endswith('x'):
            a = float(term[:-1])
        else:
            return "Error: Invalid x term"
        
        # Calculate b and c
        b = float(constant)
        c = float(right)
        
        # Solve for x
        x = (c - b) / a
        
        return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('5*x - 2 = 8'))  # Should print: 2.0
    print(tentacle('-x + 4 = 1'))   # Should print: -3.0
    print(tentacle('3*x = 9'))      # Should print: 3.0
    print(tentacle('x + 5 = 5'))    # Should print: 0.0
    print(tentacle('2*x + 3 = x'))  # Should print: -3.0
    print(tentacle('invalid'))      # Should print an error message
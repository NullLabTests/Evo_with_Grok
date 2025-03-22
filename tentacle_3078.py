# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x.
    
    Args:
    equation (str): A string containing a linear equation in the form 'ax + b = c'.
    
    Returns:
    str: The solution for x as a string.
    
    Example:
    >>> tentacle('2*x + 3 = 7')
    '2'
    """
    try:
        # Remove spaces and split the equation into left and right sides
        equation = equation.replace(" ", "")
        left, right = equation.split("=")
        
        # Parse the left side to separate the coefficient of x and the constant term
        if '+' in left:
            term1, term2 = left.split('+')
        elif '-' in left:
            term1, term2 = left.split('-')
            term2 = '-' + term2
        else:
            term1 = left
            term2 = '0'
        
        if 'x' in term1:
            a = term1.replace('x', '')
            b = term2
        else:
            a = term2.replace('x', '')
            b = term1
        
        # Convert string values to floats
        a = float(a) if a else 1.0  # If 'x' is alone, coefficient is 1
        b = float(b)
        c = float(right)
        
        # Solve for x
        x = (c - b) / a
        
        # Return the solution rounded to 2 decimal places
        return str(round(x, 2))
    
    except Exception as e:
        # Return an error message if solving fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 10'))   # Should print: 15.0
    print(tentacle('3*x = 12'))     # Should print: 4.0
    print(tentacle('x/2 = 3'))      # Should print: 6.0
    print(tentacle('2*x + 3 = x + 7'))  # Should print: 4.0
    print(tentacle('invalid equation')) # Should print an error message
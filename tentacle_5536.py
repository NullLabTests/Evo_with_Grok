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
        # Split the equation into left and right sides
        left, right = equation.split('=')
        
        # Remove whitespace
        left = left.strip()
        right = right.strip()
        
        # Parse the left side to extract coefficients
        if '+' in left:
            terms = left.split('+')
            x_term = terms[0].strip()
            constant_term = terms[1].strip()
        elif '-' in left:
            terms = left.split('-')
            x_term = terms[0].strip()
            constant_term = '-' + terms[1].strip()
        else:
            x_term = left
            constant_term = '0'
        
        # Extract the coefficient of x
        if x_term == 'x':
            a = 1
        elif x_term == '-x':
            a = -1
        else:
            a = float(x_term.replace('x', ''))
        
        # Convert constant terms to floats
        b = float(constant_term)
        c = float(right)
        
        # Solve for x
        x = (c - b) / a
        
        # Return the solution as a string
        return str(x)
    
    except Exception as e:
        # Return an error message if solving fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 10'))   # Should print: 15.0
    print(tentacle('-3*x = 9'))     # Should print: -3.0
    print(tentacle('x = 4'))        # Should print: 4.0
    print(tentacle('2*x + 3 = x'))  # Should print: -3.0
    print(tentacle('invalid'))      # Should print an error message
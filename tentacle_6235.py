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
        # Remove spaces and split the equation at '='
        left, right = equation.replace(' ', '').split('=')
        
        # Parse the left side of the equation
        if '+' in left:
            a, b = left.split('+')
        elif '-' in left:
            a, b = left.split('-')
            b = '-' + b
        else:
            a = left
            b = '0'
        
        # Extract the coefficient of x
        if a.startswith('x'):
            a = '1' + a
        elif a.endswith('x'):
            a = a[:-1]
        
        # Convert to float
        a = float(a) if a else 1.0
        b = float(b)
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
    print(tentacle('x - 5 = 0'))    # Should print: 5.0
    print(tentacle('3*x = 9'))      # Should print: 3.0
    print(tentacle('x/2 = 4'))      # Should print: 8.0
    print(tentacle('2*x + 3 = x'))  # Should print: -3.0
    print(tentacle('invalid'))      # Should print an error message
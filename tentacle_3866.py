# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x.

    Args:
    equation (str): A string containing a linear equation in the form 'a*x + b = c'.

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
        
        # Extract the coefficient of x and the constant term from the left side
        if 'x' in left:
            if '+' in left:
                a, b = left.split('+')
                a = a.strip()
                b = b.strip()
            elif '-' in left:
                a, b = left.split('-')
                a = a.strip()
                b = '-' + b.strip()
            else:
                a = left
                b = '0'
            
            # Handle cases where x is alone or has a coefficient
            if a == 'x':
                a = '1'
            elif a.endswith('x'):
                a = a[:-1]
            
            # Convert strings to numbers
            a = float(a)
            b = float(b)
            c = float(right)
            
            # Solve for x
            x = (c - b) / a
            
            # Return the solution rounded to 2 decimal places
            return str(round(x, 2))
        else:
            return "Error: No 'x' in the equation"
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 10'))   # Should print: 15.0
    print(tentacle('3*x = 12'))     # Should print: 4.0
    print(tentacle('x + 2 = 2'))    # Should print: 0.0
    print(tentacle('5 = 5'))        # Should print: Error: No 'x' in the equation
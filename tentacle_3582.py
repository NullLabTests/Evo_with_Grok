# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x and return the value of x.

    Args:
    equation (str): A string containing a linear equation in the form 'a*x + b = c'.

    Returns:
    str: The value of x as a string if the equation is solvable, otherwise an error message.

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
            a_part, b_part = left.split('+')
            a_part = a_part.strip()
            b_part = b_part.strip()
        elif '-' in left:
            a_part, b_part = left.split('-')
            a_part = a_part.strip()
            b_part = '-' + b_part.strip()
        else:
            a_part = left
            b_part = '0'
        
        # Extract coefficient of x
        if a_part.endswith('x'):
            a = float(a_part[:-1]) if a_part != 'x' else 1
        elif a_part.startswith('x'):
            a = float(a_part[1:]) if a_part != 'x' else 1
        else:
            raise ValueError("Invalid equation format")
        
        # Extract constant term
        b = float(b_part)
        
        # Calculate x
        c = float(right)
        x = (c - b) / a
        
        # Return x as a string
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
    print(tentacle('2*x + 3 = x'))  # Should print: -3.0
    print(tentacle('invalid'))      # Should print an error message
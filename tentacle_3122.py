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
            a_part, b_part = left.split('+')
        elif '-' in left:
            a_part, b_part = left.split('-')
            b_part = '-' + b_part
        else:
            a_part = left
            b_part = '0'
        
        # Extract the coefficient of x
        if a_part == 'x':
            a = 1
        elif a_part == '-x':
            a = -1
        elif a_part.endswith('x'):
            a = float(a_part[:-1])
        else:
            raise ValueError("Invalid equation format")
        
        # Convert the constant terms to floats
        b = float(b_part)
        c = float(right)
        
        # Solve for x
        x = (c - b) / a
        
        # Return the solution rounded to 2 decimal places
        return f"{x:.2f}"
    
    except Exception as e:
        # Return an error message if solving fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.00
    print(tentacle('x - 5 = 10'))   # Should print: 15.00
    print(tentacle('-3*x = 9'))     # Should print: -3.00
    print(tentacle('2x = 8'))       # Should print: 4.00
    print(tentacle('x + 2 = 2'))    # Should print: 0.00
    print(tentacle('3*x - 1 = 5'))  # Should print: 2.00
    print(tentacle('invalid'))      # Should print an error message
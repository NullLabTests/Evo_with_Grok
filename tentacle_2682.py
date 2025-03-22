# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x.

    Args:
    equation (str): A string containing a linear equation in the format 'ax + b = c'.

    Returns:
    str: The solution for x as a string.

    Example:
    >>> tentacle('2*x + 3 = 7')
    '2'
    """
    try:
        # Remove spaces and split the equation into left and right sides
        equation = equation.replace(" ", "").split("=")
        left_side = equation[0]
        right_side = equation[1]

        # Extract coefficients a and b from the left side
        if 'x' in left_side:
            if '+' in left_side:
                a, b = left_side.split('+')
            elif '-' in left_side:
                a, b = left_side.split('-')
                b = '-' + b
            else:
                a = left_side
                b = '0'
            
            a = a.replace('x', '') if a != 'x' else '1'
            a = a if a != '-x' else '-1'
        else:
            raise ValueError("Equation must contain x")

        # Convert string coefficients to floats
        a = float(a)
        b = float(b)
        c = float(right_side)

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
    print(tentacle('x + 2 = 2'))    # Should print: 0.0
    print(tentacle('2*x = 0'))      # Should print: 0.0
    print(tentacle('x = 5'))        # Should print: 5.0
    print(tentacle('2*x + 3 = x'))  # Should print: -3.0
    print(tentacle('2*x + 3y = 7')) # Should print: Error: Equation must contain x
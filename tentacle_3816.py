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
        equation = equation.replace(" ", "").split("=")
        left_side = equation[0]
        right_side = equation[1]

        # Extract coefficients and constant from the left side
        if '+' in left_side:
            parts = left_side.split('+')
            if 'x' in parts[0]:
                a = parts[0].replace('x', '')
                b = parts[1]
            else:
                a = parts[1].replace('x', '')
                b = parts[0]
        elif '-' in left_side:
            parts = left_side.split('-')
            if 'x' in parts[0]:
                a = parts[0].replace('x', '')
                b = '-' + parts[1]
            else:
                a = '-' + parts[1].replace('x', '')
                b = parts[0]
        else:
            a = left_side.replace('x', '')
            b = '0'

        # Convert coefficients to floats
        a = float(a) if a else 1.0
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
    print(tentacle('3*x = 12'))     # Should print: 4.0
    print(tentacle('x + 2 = 0'))    # Should print: -2.0
    print(tentacle('5 = 2*x - 1'))  # Should print: 3.0
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

        # Extract coefficients and constant from the left side
        if '+' in left_side:
            parts = left_side.split('+')
            if parts[0].startswith('x'):
                a = 1 if parts[0] == 'x' else float(parts[0][:-1])
                b = float(parts[1])
            else:
                a = float(parts[1][:-1])
                b = float(parts[0])
        elif '-' in left_side:
            parts = left_side.split('-')
            if parts[0].startswith('x'):
                a = 1 if parts[0] == 'x' else float(parts[0][:-1])
                b = -float(parts[1])
            else:
                a = -float(parts[1][:-1])
                b = float(parts[0])
        else:
            a = float(left_side[:-1])
            b = 0

        # Calculate x
        c = float(right_side)
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
    print(tentacle('3*x = 12'))     # Should print: 4.00
    print(tentacle('x + 2 = 0'))    # Should print: -2.00
    print(tentacle('0.5*x - 1 = 2'))# Should print: 6.00
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
        equation = equation.replace(" ", "").split("=")
        left_side = equation[0]
        right_side = equation[1]

        # Extract coefficients and constant terms
        if 'x' in left_side:
            if left_side.startswith('x'):
                a = 1
            elif left_side.startswith('-x'):
                a = -1
            else:
                a = float(left_side.split('x')[0])
        else:
            a = 0

        b = 0
        if '+' in left_side:
            b = float(left_side.split('+')[-1])
        elif '-' in left_side and 'x' in left_side.split('-')[-1]:
            b = -float(left_side.split('-')[-1])

        c = float(right_side)

        # Solve for x
        if a == 0:
            return "Error: Not a linear equation in x"
        x = (c - b) / a

        return str(x)
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 10'))  # Should print: 15.0
    print(tentacle('-3*x = 9'))  # Should print: -3.0
    print(tentacle('2 = 2'))  # Should print: Error: Not a linear equation in x
    print(tentacle('y + 2 = 4'))  # Should print: Error: Not a linear equation in x
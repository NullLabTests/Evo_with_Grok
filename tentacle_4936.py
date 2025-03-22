# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.

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

        # Extract the coefficient of x and the constant term from the left side
        if '+' in left_side:
            parts = left_side.split('+')
            if 'x' in parts[0]:
                a = eval(parts[0].replace('x', '1'))
                b = eval(parts[1])
            else:
                a = eval(parts[1].replace('x', '1'))
                b = eval(parts[0])
        elif '-' in left_side:
            parts = left_side.split('-')
            if 'x' in parts[0]:
                a = eval(parts[0].replace('x', '1'))
                b = -eval(parts[1])
            else:
                a = -eval(parts[1].replace('x', '1'))
                b = eval(parts[0])
        else:
            a = eval(left_side.replace('x', '1'))
            b = 0

        # Evaluate the right side of the equation
        c = eval(right_side)

        # Solve for x
        x = (c - b) / a

        return str(x)
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('5*x - 2 = 8'))  # Should print: 2.0
    print(tentacle('x + 4 = 10'))   # Should print: 6.0
    print(tentacle('-3*x = 9'))     # Should print: -3.0
    print(tentacle('x/2 = 5'))      # Should print: 10.0
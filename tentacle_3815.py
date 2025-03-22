# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.

    Args:
    equation (str): A string containing a linear equation in the form 'a*x + b = c'.

    Returns:
    str: The solution for x as a string, or an error message if solving fails.

    Example:
    >>> tentacle('2*x + 3 = 7')
    '2'
    """
    try:
        # Remove whitespace and split the equation into left and right sides
        equation = equation.replace(" ", "").split("=")
        left_side = equation[0]
        right_side = equation[1]

        # Extract coefficients a and b from the left side
        if '*x' in left_side:
            a, b = left_side.split('+') if '+' in left_side else left_side.split('-')
            a = a.replace('x', '') if 'x' in a else '-' + a.replace('x', '')
            b = b if b else '0'
        elif 'x' in left_side:
            a = left_side.replace('x', '') if left_side != 'x' else '1'
            b = '0'
        else:
            raise ValueError("Equation must contain 'x'")

        # Convert coefficients to floats
        a, b, c = float(a), float(b), float(right_side)

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
    print(tentacle('5*x - 2 = 8'))  # Should print: 2.0
    print(tentacle('x + 4 = 10'))   # Should print: 6.0
    print(tentacle('3*x = 15'))     # Should print: 5.0
    print(tentacle('2 = 2'))        # Should print: Error: Equation must contain 'x'
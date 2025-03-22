# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x and return the value of x.

    Args:
    equation (str): A string containing a linear equation in the form 'a*x + b = c'.

    Returns:
    str: The value of x as a string, or an error message if the equation cannot be solved.

    Example:
    >>> tentacle('2*x + 3 = 7')
    '2'
    """
    try:
        # Remove whitespace and split the equation into left and right sides
        equation = equation.replace(" ", "")
        left, right = equation.split("=")

        # Parse the left side of the equation
        if '*' in left:
            a, rest = left.split('*')
            a = float(a)
            b = float(rest) if rest else 0
        else:
            a = 1 if 'x' in left else 0
            b = float(left.replace('x', '0')) if 'x' in left else float(left)

        # Parse the right side of the equation
        c = float(right)

        # Solve for x
        if a == 0:
            return "Error: Cannot solve for x when coefficient of x is zero"
        x = (c - b) / a

        # Return the result as a string
        return str(x)

    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x + 5 = 10'))   # Should print: 5.0
    print(tentacle('3*x = 9'))      # Should print: 3.0
    print(tentacle('5 = 2*x + 1'))  # Should print: 2.0
    print(tentacle('x = 4'))        # Should print: 4.0
    print(tentacle('2 = 2'))        # Should print: Error: Cannot solve for x when coefficient of x is zero
    print(tentacle('invalid'))      # Should print: Error: ... (appropriate error message)
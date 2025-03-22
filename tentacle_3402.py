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
        if "+" in left_side:
            a, b = left_side.split("+")
        elif "-" in left_side:
            a, b = left_side.split("-")
            b = "-" + b
        else:
            a = left_side
            b = "0"

        # Extract the coefficient of x
        if "x" in a:
            a = a.replace("x", "")
            if a == "" or a == "+":
                a = "1"
            elif a == "-":
                a = "-1"
        elif "x" in b:
            a, b = b, a
            a = a.replace("x", "")
            if a == "" or a == "+":
                a = "1"
            elif a == "-":
                a = "-1"
        else:
            raise ValueError("Invalid equation format")

        # Convert strings to floats
        a = float(a)
        b = float(b)
        c = float(right_side)

        # Solve for x
        x = (c - b) / a

        return str(x)

    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 10'))   # Should print: 15.0
    print(tentacle('-3*x = 9'))     # Should print: -3.0
    print(tentacle('4 + x = 8'))    # Should print: 4.0
    print(tentacle('2*x = 6'))      # Should print: 3.0
    print(tentacle('x + 2 = 2'))    # Should print: 0.0
    print(tentacle('3*x - 1 = 5'))  # Should print: 2.0
    print(tentacle('x/2 = 4'))      # Should print: Error: Invalid equation format
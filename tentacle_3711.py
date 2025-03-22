# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.

    Args:
    equation (str): A string containing a linear equation in the form 'a*x + b = c'.

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

        # Extract coefficients and constants
        if 'x' in left:
            if '+' in left:
                a, b = left.split('+')
            elif '-' in left:
                a, b = left.split('-')
                b = '-' + b
            else:
                a = left
                b = '0'
        else:
            a = '0'
            b = left

        a = float(a.replace('x', '')) if 'x' in a else float(a)
        b = float(b)
        c = float(right)

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
    print(tentacle('5*x - 4 = 6'))  # Should print: 2.0
    print(tentacle('x + 2 = 5'))    # Should print: 3.0
    print(tentacle('3*x = 9'))      # Should print: 3.0
    print(tentacle('2 = x'))        # Should print: 2.0
    print(tentacle('x = 3'))        # Should print: 3.0
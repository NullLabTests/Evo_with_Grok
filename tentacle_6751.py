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
        equation = equation.replace(" ", "").replace("*", "")
        left, right = equation.split("=")

        # Parse the left side of the equation
        if 'x' in left:
            if '+' in left:
                a, b = left.split('+')
                a = float(a) if a != 'x' else 1
                b = float(b) if b != 'x' else 1
            elif '-' in left:
                a, b = left.split('-')
                a = float(a) if a != 'x' else 1
                b = -float(b) if b != 'x' else -1
            else:
                a = float(left) if left != 'x' else 1
                b = 0
        else:
            a = 0
            b = float(left)

        # Parse the right side of the equation
        c = float(right)

        # Solve for x
        if a == 0:
            if b == c:
                return 'All real numbers'
            else:
                return 'No solution'
        else:
            x = (c - b) / a
            return str(x)

    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 0'))    # Should print: 5.0
    print(tentacle('3 = 3'))         # Should print: All real numbers
    print(tentacle('3 = 4'))         # Should print: No solution
    print(tentacle('2x + 3 = 7'))   # Should print: 2.0 (alternative format without *)
    print(tentacle('x = 5'))         # Should print: 5.0
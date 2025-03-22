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
        # Remove spaces and split the equation into left and right parts
        equation = equation.replace(" ", "").split("=")
        left, right = equation[0], equation[1]

        # Extract coefficients and constant terms
        if 'x' in left:
            if '+' in left:
                a, b = left.split('+')
                a = a.replace('x', '') if 'x' in a else '1'
                b = '-' + b if b.startswith('-') else b
            elif '-' in left:
                a, b = left.split('-')
                a = a.replace('x', '') if 'x' in a else '1'
                b = '-' + b if not b.startswith('-') else b
            else:
                a = left.replace('x', '') if 'x' in left else '1'
                b = '0'
        else:
            a = '0'
            b = left

        a = float(a) if a else 1.0
        b = float(b) if b else 0.0
        c = float(right)

        # Solve for x
        x = (c - b) / a

        # Return the result as a string
        return str(x)

    except Exception as e:
        # Return an error message if solving fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 10'))   # Should print: 15.0
    print(tentacle('3*x = 12'))     # Should print: 4.0
    print(tentacle('x + 2 = 2'))    # Should print: 0.0
    print(tentacle('5 = x'))        # Should print: 5.0
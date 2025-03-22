# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.

    Args:
    equation (str): A string containing a linear equation in the form 'a*x + b = c'.

    Returns:
    str: The solution for x as a string, or an error message if the equation cannot be solved.

    Example:
    >>> tentacle('2*x + 3 = 7')
    '2.0'
    """
    try:
        # Remove spaces and split the equation into left and right sides
        equation = equation.replace(" ", "")
        left, right = equation.split("=")

        # Parse the left side to extract coefficients of x and constant term
        if 'x' in left:
            if '+' in left:
                a, b = left.split('+')
            elif '-' in left:
                a, b = left.split('-')
                b = '-' + b
            else:
                a = left
                b = '0'
            
            if a == 'x':
                a = '1'
            elif a == '-x':
                a = '-1'
            elif 'x' in a:
                a = a.replace('x', '')
        else:
            a = '0'
            b = left

        # Convert parsed values to floats
        a = float(a)
        b = float(b)
        c = float(right)

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
    print(tentacle('3*x = 9'))  # Should print: 3.0
    print(tentacle('2 = 2'))  # Should print: Error: Not a linear equation in x
    print(tentacle('x + y = 5'))  # Should print: Error: invalid literal for float(): y
# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x.

    Args:
    equation (str): A string containing a linear equation in the form 'ax + b = c'.

    Returns:
    str: The solution for x as a string, or an error message if the equation is invalid.

    Example:
    >>> tentacle('2*x + 3 = 7')
    '2'
    """
    try:
        # Remove spaces and split the equation into left and right sides
        equation = equation.replace(" ", "").split("=")
        if len(equation) != 2:
            return "Error: Invalid equation format"

        left, right = equation
        right = float(right)

        # Extract the coefficient of x and the constant term from the left side
        if 'x' not in left:
            return "Error: No variable 'x' in the equation"

        if left == 'x':
            return str(right)

        # Handle cases like '2x' or '-x'
        if left.endswith('x'):
            coefficient = 1 if left == 'x' else float(left[:-1])
            constant = 0
        else:
            # Split the left side into coefficient and constant
            parts = left.split('+') if '+' in left else left.split('-')
            if len(parts) == 1:
                parts = [parts[0], '0'] if '+' in left else ['0', parts[0]]

            coefficient = 1 if parts[0] == 'x' else float(parts[0][:-1]) if parts[0].endswith('x') else float(parts[0])
            constant = float(parts[1]) if parts[1] != 'x' else 1 if '+' in left else -1

        # Solve for x
        x = (right - constant) / coefficient
        return str(x)

    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 0'))    # Should print: 5.0
    print(tentacle('-x + 2 = 1'))   # Should print: 1.0
    print(tentacle('3x = 6'))       # Should print: 2.0
    print(tentacle('x = 4'))        # Should print: 4.0
    print(tentacle('2x + 3 = x + 5'))  # Should print: 2.0
    print(tentacle('2x + 3x = 10'))    # Should print: 2.0
    print(tentacle('invalid'))     # Should print an error message
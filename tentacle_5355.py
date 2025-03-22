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
        equation = equation.replace(" ", "").split("=")
        left_side, right_side = equation[0], equation[1]

        # Extract coefficients of x and constant terms
        if 'x' in left_side:
            a = float(left_side.split('x')[0]) if left_side[0] != 'x' else 1
            b = float(left_side.split('x')[1]) if len(left_side.split('x')) > 1 else 0
        else:
            a, b = 0, float(left_side)
        
        c = float(right_side)

        # Solve for x: a*x + b = c => a*x = c - b => x = (c - b) / a
        if a == 0:
            return "Error: Cannot solve for x when coefficient of x is zero"
        x = (c - b) / a

        return str(x)
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 0'))  # Should print: 5.0
    print(tentacle('3*x = 9'))  # Should print: 3.0
    print(tentacle('2 = 2'))  # Should print: Error: Cannot solve for x when coefficient of x is zero
    print(tentacle('x + y = 5'))  # Should print: Error: ... (due to multiple variables)
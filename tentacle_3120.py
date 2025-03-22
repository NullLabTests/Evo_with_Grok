# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x.

    Args:
    equation (str): A string containing a linear equation in the format 'ax + b = c'.

    Returns:
    str: The solution for x as a string, or an error message if the equation is invalid.

    Example:
    >>> tentacle('2*x + 3 = 7')
    '2'
    """
    try:
        # Remove spaces and split the equation into left and right parts
        equation = equation.replace(" ", "").split("=")
        if len(equation) != 2:
            return "Error: Invalid equation format"

        left, right = equation
        right = eval(right)

        # Extract coefficients
        if 'x' in left:
            if left == 'x':
                a = 1
                b = 0
            elif left.startswith('-x'):
                a = -1
                b = 0
            elif left.startswith('x'):
                a = 1
                b = 0
            else:
                if left.startswith('-'):
                    left = left[1:]
                    sign = -1
                else:
                    sign = 1

                parts = left.split('+')
                if len(parts) == 1:
                    parts = left.split('-')
                    parts[1] = '-' + parts[1]

                x_part = [p for p in parts if 'x' in p][0]
                a = sign * eval(x_part.replace('x', '1'))
                b = sign * sum(eval(p) for p in parts if 'x' not in p)
        else:
            a = 0
            b = eval(left)

        # Solve for x
        if a == 0:
            if b == right:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            x = (right - b) / a
            return str(x)

    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2
    print(tentacle('x - 5 = 10'))   # Should print: 15
    print(tentacle('-3*x = 9'))     # Should print: -3
    print(tentacle('5 = 5'))        # Should print: Infinite solutions
    print(tentacle('5 = 6'))        # Should print: No solution
    print(tentacle('2*x + 3 = x'))  # Should print: -3
    print(tentacle('x/2 + 3 = 7'))  # Should print: 8
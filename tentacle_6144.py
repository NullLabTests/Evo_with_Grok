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
        # Remove spaces and split the equation into left and right parts
        equation = equation.replace(" ", "").split("=")
        left, right = equation[0], equation[1]

        # Extract coefficients a and b from the left side
        if 'x' in left:
            if '+' in left:
                a, b = left.split('+')
            elif '-' in left:
                a, b = left.split('-')
                b = '-' + b
            else:
                a, b = left, '0'
            
            # Handle cases where x is not multiplied by a coefficient
            if a == 'x':
                a = '1'
            elif a == '-x':
                a = '-1'
            else:
                a = a.replace('x', '')
        else:
            # If x is not on the left side, it must be on the right
            a, b = '0', left

        # Convert string coefficients to floats
        a, b, c = float(a), float(b), float(right)

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
    print(tentacle('-x + 4 = 1'))   # Should print: 3.0
    print(tentacle('x = 5'))        # Should print: 5.0
    print(tentacle('3*x = 9'))      # Should print: 3.0
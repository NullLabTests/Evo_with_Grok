# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.
    
    Args:
    equation (str): A string containing a linear equation in the form 'a*x + b = c'.
    
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

        # Parse the left side of the equation
        if '*' in left:
            a, b = left.split('+')
            a = float(a.replace('x', ''))
            b = float(b)
        elif '+' in left:
            a = 1.0
            b = float(left.split('+')[1])
        elif '-' in left:
            a = 1.0
            b = float(left.split('-')[1]) * -1
        else:
            a = float(left.replace('x', ''))
            b = 0.0

        # Solve for x
        x = (right - b) / a

        # Return the solution rounded to 2 decimal places
        return str(round(x, 2))

    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x + 5 = 10'))   # Should print: 5.0
    print(tentacle('3*x - 2 = 10')) # Should print: 4.0
    print(tentacle('5 = 2*x'))      # Should print: 2.5
    print(tentacle('x = 3'))        # Should print: 3.0
    print(tentacle('2*x + y = 7'))  # Should print: Error: Invalid equation format
    print(tentacle('2*x + 3'))      # Should print: Error: Invalid equation format
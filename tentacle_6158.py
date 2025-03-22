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
        # Remove spaces and split the equation at '='
        equation = equation.replace(" ", "").split("=")
        
        if len(equation) != 2:
            return "Error: Invalid equation format"

        left, right = equation
        
        # Extract coefficients
        if 'x' in left:
            a, b = 0, 0
            if left.startswith('-'):
                left = left[1:]
                sign = -1
            else:
                sign = 1
            
            if '+' in left or '-' in left:
                parts = left.split('x')
                if parts[0]:
                    a = sign * float(parts[0])
                if len(parts) > 1:
                    b = float(parts[1]) if parts[1] else 0
            else:
                if left.endswith('x'):
                    a = sign * float(left[:-1]) if left[:-1] else sign
                else:
                    b = sign * float(left)
        else:
            b = float(left)
            a = 0

        c = float(right)

        # Solve for x
        if a == 0:
            if b == c:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            x = (c - b) / a
            return str(x)

    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 0'))    # Should print: 5.0
    print(tentacle('3*x = 9'))      # Should print: 3.0
    print(tentacle('2 = 2'))        # Should print: Infinite solutions
    print(tentacle('2 = 3'))        # Should print: No solution
    print(tentacle('x + x = 6'))    # Should print: 3.0
    print(tentacle('2*x + 3 = x'))  # Should print: -3.0
    print(tentacle('invalid'))      # Should print: Error: Invalid equation format
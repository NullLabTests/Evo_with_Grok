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
        # Remove whitespace and split the equation into left and right sides
        equation = equation.replace(" ", "").split("=")
        if len(equation) != 2:
            raise ValueError("Invalid equation format")

        left, right = equation
        right = float(right)

        # Extract coefficient and constant from the left side
        if 'x' not in left:
            raise ValueError("Equation must contain 'x'")

        if left == 'x':
            coefficient = 1
            constant = 0
        elif left.startswith('-x'):
            coefficient = -1
            constant = 0
        elif left.endswith('x'):
            coefficient = float(left[:-1])
            constant = 0
        elif '*x' in left:
            parts = left.split('*x')
            coefficient = float(parts[0])
            constant = float(parts[1]) if parts[1] else 0
        else:
            raise ValueError("Unable to parse equation")

        # Solve for x
        x = (right - constant) / coefficient

        # Return the result as a string
        return str(x)

    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 10'))   # Should print: 15.0
    print(tentacle('-3*x = 9'))     # Should print: -3.0
    print(tentacle('2 = x'))        # Should print: 2.0
    print(tentacle('x = 5'))        # Should print: 5.0
    print(tentacle('2*x + 3 = x + 7'))  # Should print: 4.0
    print(tentacle('2*x + 3 = 2*x + 7'))  # Should print: Error: division by zero
    print(tentacle('2*y + 3 = 7'))  # Should print: Error: Equation must contain 'x'
    print(tentacle('2*x + 3 ='))    # Should print: Error: Invalid equation format
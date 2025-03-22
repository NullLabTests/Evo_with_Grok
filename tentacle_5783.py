# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x and return the value of x as a string.
    
    Args:
    equation (str): A string containing a linear equation in the form 'ax + b = c'.
    
    Returns:
    str: The value of x as a string, or an error message if the equation is invalid.
    
    Example:
    >>> tentacle('2*x + 3 = 7')
    '2'
    >>> tentacle('5*x - 4 = 11')
    '3'
    """
    try:
        # Remove whitespace and split the equation into left and right sides
        equation = equation.replace(" ", "").split("=")
        if len(equation) != 2:
            raise ValueError("Invalid equation format")

        left, right = equation
        right = float(right)

        # Extract coefficients of x and constant term from the left side
        import re
        x_term = re.search(r'([+-]?\d*\.?\d*)?\*?x', left)
        constant_term = re.search(r'([+-]?\d*\.?\d*)', left.replace(x_term.group() if x_term else '', ''))

        a = float(x_term.group(1) if x_term.group(1) else 1 if x_term.group(0) in ['x', '+x'] else -1 if x_term.group(0) == '-x' else 0)
        b = float(constant_term.group(1) if constant_term else 0)

        # Solve for x
        x = (right - b) / a

        # Return x as a string, rounded to 2 decimal places
        return f"{x:.2f}"

    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.00
    print(tentacle('5*x - 4 = 11'))  # Should print: 3.00
    print(tentacle('x = 5'))  # Should print: 5.00
    print(tentacle('-2*x + 3 = 7'))  # Should print: -2.00
    print(tentacle('0.5*x - 1 = 2'))  # Should print: 6.00
    print(tentacle('2*x + 3 = 3'))  # Should print: 0.00
    print(tentacle('invalid equation'))  # Should print an error message
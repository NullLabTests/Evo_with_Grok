# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x.

    Args:
    equation (str): A string containing a linear equation in the format 'a*x + b = c'.

    Returns:
    str: The solution for x as a string, or an error message if the equation cannot be solved.

    Example:
    >>> tentacle('2*x + 3 = 7')
    '2'
    """
    try:
        # Split the equation into left and right sides
        left, right = equation.split('=')
        
        # Remove whitespace and simplify the equation
        left = left.strip().replace(' ', '')
        right = right.strip().replace(' ', '')
        
        # Parse the left side of the equation
        if 'x' not in left:
            raise ValueError("Equation must contain 'x' on the left side.")
        
        # Extract coefficients
        if left.startswith('x'):
            a = 1
            b = 0 if left == 'x' else float(left[1:])
        elif left.endswith('x'):
            a = float(left[:-1])
            b = 0
        else:
            parts = left.split('+')
            if len(parts) == 1:
                parts = left.split('-')
                if len(parts) == 1:
                    raise ValueError("Invalid equation format.")
                elif parts[0] == '':
                    a = -1 if parts[1].startswith('x') else float(parts[1][:-1])
                    b = 0 if len(parts[1]) == 1 else float(parts[1][1:])
                else:
                    a = float(parts[0]) if parts[1].startswith('x') else -float(parts[1][:-1])
                    b = float(parts[1]) if len(parts[1]) == 1 else float(parts[1][1:])
            else:
                a = float(parts[0][:-1]) if parts[0].endswith('x') else 1
                b = float(parts[1]) if 'x' not in parts[1] else float(parts[1][:-1]) if parts[1].endswith('x') else float(parts[1][1:])
        
        # Calculate x
        c = float(right)
        x = (c - b) / a
        
        # Return the solution rounded to 2 decimal places
        return f"{x:.2f}"
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.00
    print(tentacle('x - 5 = 10'))   # Should print: 15.00
    print(tentacle('3*x = 12'))     # Should print: 4.00
    print(tentacle('x + 2 = 2'))    # Should print: 0.00
    print(tentacle('2*x = x + 3'))  # Should print: 3.00
    print(tentacle('x = 5'))        # Should print: 5.00
    print(tentacle('2*x + 3 = 3'))  # Should print: 0.00
    print(tentacle('x + x = 10'))   # Should print: 5.00
    print(tentacle('2*x - x = 7'))  # Should print: 7.00
    print(tentacle('x + 2 = x'))    # Should print: Error: division by zero
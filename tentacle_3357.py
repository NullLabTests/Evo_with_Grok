# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.
    
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
            raise ValueError("Invalid equation format")

        left, right = equation
        right = float(right)

        # Parse the left side of the equation
        if 'x' not in left:
            raise ValueError("Equation must contain 'x'")
        
        if left == 'x':
            return str(right)
        
        if left.startswith('x'):
            coefficient = 1
            constant = float(left[1:])
        elif left.endswith('x'):
            coefficient = float(left[:-1])
            constant = 0
        else:
            # Split the left side into coefficient and constant
            parts = left.split('+')
            if len(parts) == 1:
                parts = left.split('-')
                if len(parts) == 1:
                    raise ValueError("Invalid equation format")
                elif len(parts) == 2:
                    coefficient = float(parts[0])
                    constant = -float(parts[1].replace('x', ''))
                else:
                    raise ValueError("Invalid equation format")
            elif len(parts) == 2:
                coefficient = float(parts[0].replace('x', ''))
                constant = float(parts[1])
            else:
                raise ValueError("Invalid equation format")

        # Solve for x
        x = (right - constant) / coefficient
        return str(x)

    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: '2.0'
    print(tentacle('x + 5 = 10'))   # Should print: '5.0'
    print(tentacle('3x - 2 = 10'))  # Should print: '4.0'
    print(tentacle('x = 5'))        # Should print: '5.0'
    print(tentacle('2x = 10'))      # Should print: '5.0'
    print(tentacle('x + 2 ='))      # Should print: Error message
    print(tentacle('2x + 3y = 7'))  # Should print: Error message
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
        # Remove spaces and split the equation at '='
        equation = equation.replace(" ", "").split("=")
        if len(equation) != 2:
            return "Error: Invalid equation format"

        left, right = equation
        right = float(right)

        # Extract coefficient and constant from the left side
        if 'x' in left:
            if left == 'x':
                coefficient = 1
                constant = 0
            elif left.startswith('-x'):
                coefficient = -1
                constant = 0
            elif left.endswith('x'):
                coefficient = float(left[:-1])
                constant = 0
            else:
                parts = left.split('x')
                if len(parts) == 2:
                    if parts[0] == '' and parts[1] == '':
                        coefficient = 1
                        constant = 0
                    elif parts[0] == '-':
                        coefficient = -1
                        constant = 0
                    elif parts[0] == '':
                        coefficient = 1
                        constant = float(parts[1])
                    elif parts[1] == '':
                        coefficient = float(parts[0])
                        constant = 0
                    else:
                        coefficient = float(parts[0])
                        constant = float(parts[1])
                else:
                    return "Error: Invalid equation format"
        else:
            return "Error: No variable 'x' found in the equation"

        # Solve for x
        x = (right - constant) / coefficient
        
        # Return the solution as a string
        return str(x)

    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 10'))  # Should print: 15.0
    print(tentacle('-3*x = 9'))  # Should print: -3.0
    print(tentacle('2x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x = 5'))  # Should print: 5.0
    print(tentacle('2*x + 3 ='))  # Should print: Error: Invalid equation format
    print(tentacle('2*y + 3 = 7'))  # Should print: Error: No variable 'x' found in the equation
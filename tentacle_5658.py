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
        if 'x' not in left:
            return "Error: No variable 'x' found in the equation"
        
        # Handle cases with or without coefficient
        if left == 'x':
            return str(right)
        elif left.startswith('x'):
            coefficient = 1
            constant = 0
        elif left.endswith('x'):
            coefficient = float(left[:-1])
            constant = 0
        else:
            parts = left.split('+')
            if len(parts) == 1:
                parts = left.split('-')
                if len(parts) == 1:
                    return "Error: Invalid equation format"
                elif parts[1].endswith('x'):
                    coefficient = -float(parts[1][:-1])
                    constant = float(parts[0])
                else:
                    return "Error: Invalid equation format"
            elif parts[1].endswith('x'):
                coefficient = float(parts[1][:-1])
                constant = float(parts[0])
            else:
                return "Error: Invalid equation format"
        
        # Solve for x
        x = (right - constant) / coefficient
        return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x + 5 = 10'))  # Should print: 5.0
    print(tentacle('-3*x = 9'))  # Should print: -3.0
    print(tentacle('5 = 2*x - 1'))  # Should print: 3.0
    print(tentacle('x = 4'))  # Should print: 4.0
    print(tentacle('2*y + 3 = 7'))  # Should print: Error: No variable 'x' found in the equation
    print(tentacle('2*x + 3'))  # Should print: Error: Invalid equation format
    print(tentacle('2*x + 3 ='))  # Should print: Error: Invalid equation format
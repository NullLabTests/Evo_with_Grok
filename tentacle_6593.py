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
        # Remove spaces and split the equation into left and right sides
        equation = equation.replace(" ", "").split("=")
        if len(equation) != 2:
            raise ValueError("Invalid equation format")
        
        left, right = equation
        right = float(right)
        
        # Parse the left side of the equation
        if 'x' not in left:
            raise ValueError("Equation must contain x")
        
        # Extract coefficient of x and constant term
        if left.startswith('x'):
            coeff = 1 if left == 'x' else float(left[0])
            constant = 0
        elif left.endswith('x'):
            coeff = float(left[:-1])
            constant = 0
        else:
            parts = left.split('+')
            if len(parts) == 1:
                parts = left.split('-')
                if len(parts) == 1:
                    raise ValueError("Invalid equation format")
                elif parts[1].endswith('x'):
                    coeff = -float(parts[1][:-1])
                    constant = float(parts[0])
                else:
                    raise ValueError("Invalid equation format")
            elif len(parts) == 2:
                if parts[0].endswith('x'):
                    coeff = float(parts[0][:-1])
                    constant = float(parts[1])
                elif parts[1].endswith('x'):
                    coeff = float(parts[1][:-1])
                    constant = float(parts[0])
                else:
                    raise ValueError("Invalid equation format")
            else:
                raise ValueError("Invalid equation format")
        
        # Solve for x
        x = (right - constant) / coeff
        
        return str(x)
    
    except ValueError as e:
        return f"Error: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 10'))   # Should print: 15.0
    print(tentacle('3x = 12'))      # Should print: 4.0
    print(tentacle('x + 2 = 2'))    # Should print: 0.0
    print(tentacle('2x + 3 = 3x'))  # Should print: 3.0
    print(tentacle('x = 5'))        # Should print: 5.0
    print(tentacle('2*x + 3'))      # Should print: Error: Invalid equation format
    print(tentacle('2*y + 3 = 7'))  # Should print: Error: Equation must contain x
    print(tentacle('2x + 3y = 7'))  # Should print: Error: Invalid equation format
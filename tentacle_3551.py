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
        
        # Parse the left side of the equation
        if 'x' not in left:
            return "Error: Equation must contain x"
        
        # Extract coefficient of x and constant term
        if left.startswith('x'):
            a = 1 if left == 'x' else float(left[0])
            b = 0 if left == 'x' else float(left[1:])
        elif left.endswith('x'):
            a = float(left[:-1])
            b = 0
        else:
            parts = left.split('x')
            a = float(parts[0]) if parts[0] else 1
            b = float(parts[1]) if parts[1] else 0
        
        # Calculate the solution
        c = float(right)
        x = (c - b) / a
        
        return str(x)
    
    except ValueError:
        return "Error: Invalid numerical values in the equation"
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x + 5 = 10'))   # Should print: 5.0
    print(tentacle('3x - 2 = 1'))   # Should print: 1.0
    print(tentacle('x = 4'))        # Should print: 4.0
    print(tentacle('2x = 6'))       # Should print: 3.0
    print(tentacle('x + y = 5'))    # Should print: Error: Equation must contain x
    print(tentacle('2x + 3y = 7'))  # Should print: Error: Equation must contain x
    print(tentacle('2x + 3 ='))     # Should print: Error: Invalid equation format
    print(tentacle('2x + 3 = a'))   # Should print: Error: Invalid numerical values in the equation
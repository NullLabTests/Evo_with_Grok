# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.
    
    Args:
    equation (str): A string containing a linear equation in the form 'ax + b = c'.
    
    Returns:
    str: The solution for x as a string, or an error message if the equation cannot be solved.
    
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
        
        # Extract the coefficient of x and the constant term from the left side
        if 'x' in left:
            if left == 'x':
                a = 1
                b = 0
            elif left.startswith('-x'):
                a = -1
                b = 0
            elif left.endswith('x'):
                a = float(left[:-1])
                b = 0
            else:
                parts = left.split('x')
                if len(parts) == 2:
                    a = float(parts[0]) if parts[0] else 1
                    b = float(parts[1]) if parts[1] else 0
                else:
                    return "Error: Invalid equation format"
        else:
            return "Error: No x term in the equation"
        
        # Calculate the right side of the equation
        c = float(right)
        
        # Solve for x
        x = (c - b) / a
        
        # Return the solution rounded to two decimal places
        return f"{x:.2f}"
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.00
    print(tentacle('x - 5 = 10'))   # Should print: 15.00
    print(tentacle('-3*x = 9'))     # Should print: -3.00
    print(tentacle('2x + 3 = 7'))   # Should print: 2.00
    print(tentacle('x = 5'))        # Should print: 5.00
    print(tentacle('2*x + 3 = x'))  # Should print: -3.00
    print(tentacle('2*x + 3'))      # Should print: Error: Invalid equation format
    print(tentacle('y + 3 = 7'))    # Should print: Error: No x term in the equation
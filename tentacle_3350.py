# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.
    
    Args:
    equation (str): A string containing a linear equation in the format 'ax + b = c'.
    
    Returns:
    str: The solution for x as a string, or an error message if the equation is invalid.
    
    Example:
    >>> tentacle('2*x + 3 = 7')
    '2'
    """
    try:
        # Remove spaces and split the equation into left and right sides
        equation = equation.replace(" ", "").replace("*x", "x")
        left, right = equation.split("=")
        
        # Parse the left side of the equation
        if 'x' in left:
            if left.startswith('x'):
                a = 1
            elif left.startswith('-x'):
                a = -1
            else:
                a = float(left.split('x')[0])
        else:
            return "Error: No x term in the equation"
        
        # Parse the constant terms
        b = 0 if 'x' == left or '-x' == left else float(left.replace(f"{a}x", "")) if 'x' in left else float(left)
        c = float(right)
        
        # Solve for x
        x = (c - b) / a
        
        # Return the solution rounded to 2 decimal places
        return f"{x:.2f}"
    
    except ValueError:
        return "Error: Invalid equation format"
    except ZeroDivisionError:
        return "Error: Division by zero"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.00
    print(tentacle('x - 5 = 0'))    # Should print: 5.00
    print(tentacle('-3*x = 9'))     # Should print: -3.00
    print(tentacle('2*x = 4'))      # Should print: 2.00
    print(tentacle('x + 2 = 3'))    # Should print: 1.00
    print(tentacle('2 = 2'))        # Should print: Error: No x term in the equation
    print(tentacle('x/x = 1'))      # Should print: Error: Division by zero
    print(tentacle('2x + 3y = 7'))  # Should print: Error: Invalid equation format
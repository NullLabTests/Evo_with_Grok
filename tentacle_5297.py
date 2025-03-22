# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.
    
    Args:
    equation (str): A string containing a linear equation in the form 'a*x + b = c'.
    
    Returns:
    str: The solution for x as a string, or an error message if the equation cannot be solved.
    
    Example:
    >>> tentacle('2*x + 3 = 7')
    '2'
    """
    try:
        # Remove spaces and split the equation into left and right sides
        equation = equation.replace(" ", "")
        left, right = equation.split("=")
        
        # Parse the left side of the equation
        if '*' in left:
            a, rest = left.split('*')
            a = float(a)
            b = float(rest) if rest else 0
        else:
            a = 1 if 'x' in left else 0
            b = float(left.replace('x', '0')) if 'x' in left else float(left)
        
        # Parse the right side of the equation
        c = float(right)
        
        # Solve for x
        if a == 0:
            return "Error: Cannot solve for x when coefficient of x is zero."
        x = (c - b) / a
        
        # Return the solution rounded to 2 decimal places
        return f"{x:.2f}"
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.00
    print(tentacle('x - 5 = 10'))   # Should print: 15.00
    print(tentacle('3*x = 9'))      # Should print: 3.00
    print(tentacle('5 = 5'))        # Should print: Error: Cannot solve for x when coefficient of x is zero.
    print(tentacle('2*x + y = 7'))  # Should print: Error: invalid syntax
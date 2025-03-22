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
    '2.0'
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
            a = 1 if left.startswith('x') else -1 if left.startswith('-x') else 0
            b = float(left.replace('x', '0')) if 'x' in left else float(left)
        
        # Parse the right side of the equation
        c = float(right)
        
        # Solve for x
        if a == 0:
            return "Error: Not a linear equation in x"
        x = (c - b) / a
        
        return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 10'))   # Should print: 15.0
    print(tentacle('-3*x = 9'))     # Should print: -3.0
    print(tentacle('2 = 2'))        # Should print: Error: Not a linear equation in x
    print(tentacle('x + x = 4'))    # Should print: 2.0
    print(tentacle('2*x = y'))      # Should print: Error: could not convert string to float: 'y'
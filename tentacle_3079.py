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
            return "Error: Invalid equation format"
        
        left, right = equation
        
        # Extract coefficients of x and constant terms
        import re
        left_parts = re.findall(r'([+-]?\d*\.?\d*)x?|\+|-', left)
        right_parts = re.findall(r'([+-]?\d*\.?\d*)x?|\+|-', right)
        
        a = sum(float(part) for part in left_parts if 'x' in part)
        b = sum(float(part) for part in left_parts if 'x' not in part and part not in ['+', '-'])
        c = sum(float(part) for part in right_parts if 'x' not in part and part not in ['+', '-'])
        
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
    print(tentacle('3*x = 9'))      # Should print: 3.0
    print(tentacle('x + 2 = 2'))    # Should print: 0.0
    print(tentacle('2*x + 3 = x'))  # Should print: -3.0
    print(tentacle('x = 5'))        # Should print: 5.0
    print(tentacle('2*x + y = 7'))  # Should print: Error: Invalid equation format
    print(tentacle('2*x + 3 ='))    # Should print: Error: Invalid equation format
    print(tentacle('2 = 2'))        # Should print: Error: Not a linear equation in x
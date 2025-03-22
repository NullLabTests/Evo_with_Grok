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
        if '*' in left:
            a, b = left.split('*')
            a = float(a)
            b = float(b)
        else:
            a = 1.0
            b = float(left)
        
        # Solve for x
        x = (right - b) / a
        
        # Return the solution rounded to 2 decimal places
        return f"{x:.2f}"
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.00
    print(tentacle('x + 5 = 10'))   # Should print: 5.00
    print(tentacle('3*x = 9'))      # Should print: 3.00
    print(tentacle('x - 2 = 0'))    # Should print: 2.00
    print(tentacle('2*x + 3 = x'))  # Should print: -3.00
    print(tentacle('invalid'))      # Should print: Error: Invalid equation format
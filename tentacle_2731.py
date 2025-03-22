# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.
    
    Args:
    equation (str): A string containing a linear equation in the form 'a*x + b = c'.
    
    Returns:
    str: The value of x as a string, or an error message if the equation is invalid.
    
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
        if 'x' in left:
            a, b = map(float, left.split('*x') + ['0'] if '+' in left or '-' in left else ['1', '0'])
        else:
            a, b = 0, float(left)
        
        c = float(right)
        
        # Solve for x
        if a == 0:
            return "Error: Not a linear equation in x"
        
        x = (c - b) / a
        
        # Return x rounded to 2 decimal places
        return f"{x:.2f}"
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.00
    print(tentacle('5*x - 2 = 8'))  # Should print: 2.00
    print(tentacle('x + 1 = 0'))    # Should print: -1.00
    print(tentacle('3 = 3*x'))      # Should print: 1.00
    print(tentacle('2*x = 4'))      # Should print: 2.00
    print(tentacle('x = 5'))        # Should print: 5.00
    print(tentacle('2*y + 3 = 7'))  # Should print: Error: Invalid equation format
    print(tentacle('2*x + 3 = x'))  # Should print: Error: Not a linear equation in x
    print(tentacle('2*x + 3 = a'))  # Should print: Error: could not convert string to float: 'a'
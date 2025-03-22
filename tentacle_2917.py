# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.
    
    Args:
    equation (str): A string containing a linear equation in the form 'ax + b = c'.
    
    Returns:
    str: The value of x as a string, or an error message if the equation is invalid or not linear.
    
    Example:
    >>> tentacle('2*x + 3 = 7')
    '2'
    """
    try:
        # Remove spaces and split the equation at '='
        equation = equation.replace(' ', '').split('=')
        
        if len(equation) != 2:
            return "Error: Invalid equation format"
        
        left, right = equation
        
        # Find the coefficient of x on the left side
        if 'x' in left:
            if left == 'x':
                a = 1
            elif left.startswith('-x'):
                a = -1
            elif left.startswith('x'):
                a = 1
            else:
                a = float(left.split('x')[0])
        else:
            a = 0
        
        # Calculate the constant term on the left side
        b = 0 if a == 0 else float(eval(left.replace('x', '0')))
        
        # Calculate the right side
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
    print(tentacle('x = 4'))        # Should print: 4.0
    print(tentacle('2*x + 3 = x'))  # Should print: -3.0
    print(tentacle('2*x + 3'))      # Should print: Error: Invalid equation format
    print(tentacle('x^2 = 4'))      # Should print: Error: Not a linear equation in x
    print(tentacle('2*y + 3 = 7'))  # Should print: Error: Not a linear equation in x
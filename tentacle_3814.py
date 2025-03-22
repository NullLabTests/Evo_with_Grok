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
        equation = equation.replace(" ", "")
        left, right = equation.split("=")
        
        # Parse the left side of the equation
        if 'x' in left:
            if '+' in left:
                a, b = left.split('+')
            elif '-' in left:
                a, b = left.split('-')
                b = '-' + b
            else:
                a = left
                b = '0'
            
            # Extract coefficient of x
            if a == 'x':
                a = '1'
            elif a == '-x':
                a = '-1'
            else:
                a = a.replace('x', '')
            
            a = float(a)
            b = float(b)
            c = float(right)
            
            # Solve for x
            x = (c - b) / a
            
            return str(x)
        else:
            return "Error: Equation does not contain x"
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('5 - x = 2'))    # Should print: 3.0
    print(tentacle('x = 4'))        # Should print: 4.0
    print(tentacle('2*x = 6'))      # Should print: 3.0
    print(tentacle('3 + 2 = 5'))    # Should print: Error: Equation does not contain x
    print(tentacle('x^2 + 2 = 5'))  # Should print: Error: Equation does not contain x
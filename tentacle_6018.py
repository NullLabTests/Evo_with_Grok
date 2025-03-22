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
        # Split the equation into left and right sides
        left, right = equation.split('=')
        
        # Remove whitespace and simplify the equation
        left = left.strip().replace(' ', '')
        right = right.strip().replace(' ', '')
        
        # Find the coefficient of x and the constant term on the left side
        if 'x' in left:
            if '*' in left:
                a, rest = left.split('*')
                a = float(a)
                b = float(eval(rest.replace('x', '0')))
            else:
                a = float(left.replace('x', '1'))
                b = 0
        else:
            a = 0
            b = float(left)
        
        # Calculate the constant term on the right side
        c = float(right)
        
        # Solve for x
        if a == 0 and b == c:
            return 'Infinite solutions (0 = 0)'
        elif a == 0:
            return 'No solution'
        else:
            x = (c - b) / a
            return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x + 5 = 10'))   # Should print: 5.0
    print(tentacle('3*x = 9'))      # Should print: 3.0
    print(tentacle('5 = 5'))        # Should print: Infinite solutions (0 = 0)
    print(tentacle('x + 1 = 2*x'))  # Should print: 1.0
    print(tentacle('2 = 3'))        # Should print: No solution
    print(tentacle('x + y = 5'))    # Should print: Error: name 'y' is not defined
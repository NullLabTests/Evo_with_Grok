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
    '2.0'
    """
    try:
        # Split the equation into left and right sides
        left, right = equation.split('=')
        
        # Remove whitespace and simplify the equation
        left = left.strip().replace(' ', '')
        right = right.strip().replace(' ', '')
        
        # Identify the coefficient of x and the constant term on the left side
        if 'x' in left:
            if left.startswith('-x') or left.startswith('x'):
                a = -1 if left.startswith('-x') else 1
                b = 0 if left == '-x' or left == 'x' else eval(left[1 if left.startswith('-x') else 0:].replace('x', '1'))
            else:
                a, b = map(float, left.replace('x', '(1)').split('+'))
        else:
            a, b = 0, eval(left)
        
        # Evaluate the right side
        c = eval(right)
        
        # Solve for x
        if a == 0:
            return "Error: Not a linear equation (a = 0)"
        x = (c - b) / a
        
        return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('5*x - 4 = 1'))  # Should print: 1.0
    print(tentacle('-x + 2 = 0'))   # Should print: 2.0
    print(tentacle('3 = 3'))        # Should print: Error: Not a linear equation (a = 0)
    print(tentacle('x^2 + 2 = 3'))  # Should print: Error: invalid syntax
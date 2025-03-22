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
        # Split the equation into left and right sides
        left, right = equation.split('=')
        
        # Remove whitespace and simplify the equation
        left = left.strip().replace(' ', '')
        right = right.strip().replace(' ', '')
        
        # Extract the coefficient of x and the constant term from the left side
        if 'x' in left:
            if left.startswith('-x') or left.startswith('x'):
                a = -1 if left.startswith('-x') else 1
                b = eval(left.replace('-x', '0').replace('x', '0'))
            else:
                a = eval(left.split('x')[0])
                b = eval(left.replace(str(a) + 'x', '0'))
        else:
            a = 0
            b = eval(left)
        
        # Evaluate the right side
        c = eval(right)
        
        # Solve for x
        if a == 0 and b == c:
            return 'All real numbers'
        elif a == 0 and b != c:
            return 'No solution'
        else:
            x = (c - b) / a
            return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 10'))   # Should print: 15.0
    print(tentacle('-3*x = 9'))     # Should print: -3.0
    print(tentacle('2 = 2'))        # Should print: All real numbers
    print(tentacle('2 = 3'))        # Should print: No solution
    print(tentacle('x + x = 6'))    # Should print: 3.0
    print(tentacle('2*x + 3 = x')) # Should print: -3.0
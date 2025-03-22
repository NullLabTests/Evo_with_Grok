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
        
        # Remove whitespace and evaluate both sides
        left = eval(left.replace('x', '(x)'))
        right = eval(right)
        
        # Isolate x term on one side
        if callable(left):
            equation = f'(x) = {right - left(0)}'
        else:
            equation = f'(x) = {left - right}'
        
        # Extract coefficient of x
        x_term = equation.split('=')[0].strip('()')
        coefficient = eval(x_term) if x_term != 'x' else 1
        
        # Solve for x
        solution = str(equation.split('=')[1].strip() / coefficient)
        
        return solution
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: '2'
    print(tentacle('5 - x = 2'))  # Should print: '3'
    print(tentacle('3*x = 9'))  # Should print: '3'
    print(tentacle('x + 2 = 5'))  # Should print: '3'
    print(tentacle('2*x - 4 = 0'))  # Should print: '2'
    print(tentacle('invalid equation'))  # Should print an error message
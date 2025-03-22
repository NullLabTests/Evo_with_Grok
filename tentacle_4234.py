# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.
    
    Args:
    equation (str): A string containing a linear equation in the form 'ax + b = c'.
    
    Returns:
    str: The solution for x as a string.
    
    Example:
    >>> tentacle('2*x + 3 = 7')
    '2'
    """
    try:
        # Remove spaces and split the equation into left and right parts
        equation = equation.replace(" ", "").split("=")
        left, right = equation[0], equation[1]
        
        # Isolate the x term on the left side
        if '+' in left:
            left_parts = left.split('+')
            constant = sum(float(part) for part in left_parts if 'x' not in part)
            x_term = next(part for part in left_parts if 'x' in part)
        elif '-' in left:
            left_parts = left.split('-')
            constant = float(left_parts[0]) - sum(float(part) for part in left_parts[1:] if 'x' not in part)
            x_term = left_parts[0] if 'x' in left_parts[0] else '-' + next(part for part in left_parts[1:] if 'x' in part)
        else:
            x_term = left
            constant = 0
        
        # Extract the coefficient of x
        if x_term == 'x':
            a = 1
        elif x_term == '-x':
            a = -1
        else:
            a = float(x_term.replace('x', ''))
        
        # Calculate the right side of the equation
        b = float(right) - constant
        
        # Solve for x
        x = b / a
        
        return str(x)
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: '2.0'
    print(tentacle('3*x - 4 = 5'))  # Should print: '3.0'
    print(tentacle('x + 2 = 6'))    # Should print: '4.0'
    print(tentacle('-x + 1 = 0'))   # Should print: '1.0'
    print(tentacle('5*x = 10'))     # Should print: '2.0'
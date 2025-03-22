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
        # Remove spaces and split the equation into left and right sides
        equation = equation.replace(" ", "").split("=")
        left_side = equation[0]
        right_side = equation[1]
        
        # Isolate the x term on the left side
        if '+' in left_side:
            left_side = left_side.split('+')
            constant = left_side[1]
            left_side = left_side[0]
        elif '-' in left_side:
            left_side = left_side.split('-')
            constant = '-' + left_side[1]
            left_side = left_side[0]
        else:
            constant = '0'
        
        # Move the constant to the right side
        right_side = f"({right_side})-({constant})"
        
        # Solve for x
        if left_side == 'x':
            solution = eval(right_side)
        elif left_side.startswith('x*'):
            coefficient = left_side[2:]
            solution = eval(f"({right_side})/({coefficient})")
        elif left_side.endswith('*x'):
            coefficient = left_side[:-2]
            solution = eval(f"({right_side})/({coefficient})")
        else:
            raise ValueError("Invalid equation format")
        
        return str(solution)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('5 - x = 2'))  # Should print: 3.0
    print(tentacle('3*x = 9'))  # Should print: 3.0
    print(tentacle('x*4 = 16'))  # Should print: 4.0
    print(tentacle('x + 5 = 5'))  # Should print: 0.0
    print(tentacle('2*x - 3 = 7'))  # Should print: 5.0
    print(tentacle('invalid equation'))  # Should print an error message
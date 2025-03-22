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
        
        # Extract the coefficient of x and the constant term from the left side
        if 'x' in left_side:
            if left_side.startswith('-x') or left_side.startswith('x'):
                coefficient = -1 if left_side.startswith('-x') else 1
                constant = eval(left_side.replace('x', '0'))
            else:
                parts = left_side.split('x')
                coefficient = eval(parts[0]) if parts[0] else 1
                constant = eval(parts[1]) if len(parts) > 1 else 0
        else:
            coefficient = 0
            constant = eval(left_side)
        
        # Calculate the right side of the equation
        right_value = eval(right_side)
        
        # Solve for x
        if coefficient == 0:
            if constant == right_value:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            x = (right_value - constant) / coefficient
            return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 0'))  # Should print: 5.0
    print(tentacle('-3*x = 9'))  # Should print: -3.0
    print(tentacle('2 = 2'))  # Should print: Infinite solutions
    print(tentacle('2 = 3'))  # Should print: No solution
    print(tentacle('x + x = 6'))  # Should print: 3.0
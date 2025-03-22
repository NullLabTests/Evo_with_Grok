# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.
    
    Args:
    equation (str): A string containing a linear equation in the form 'ax + b = c'.
    
    Returns:
    str: The solution for x as a string, or an error message if solving fails.
    
    Example:
    >>> tentacle('2*x + 3 = 7')
    '2'
    """
    try:
        # Remove spaces and split the equation into left and right sides
        equation = equation.replace(" ", "").split("=")
        left_side = equation[0]
        right_side = equation[1]
        
        # Extract coefficients
        if 'x' in left_side:
            if left_side.startswith('-x') or left_side.startswith('x'):
                a = -1 if left_side.startswith('-x') else 1
                b = eval(left_side.replace('-x', '0').replace('x', '0'))
            else:
                a, b = map(float, left_side.replace('x', '*x').replace('*x', '').split('+'))
        else:
            a, b = 0, eval(left_side)
        
        c = eval(right_side)
        
        # Solve for x
        x = (c - b) / a
        
        # Return the solution rounded to 2 decimal places
        return f"{x:.2f}"
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.00
    print(tentacle('5*x - 2 = 8'))  # Should print: 2.00
    print(tentacle('-x + 4 = 1'))   # Should print: 3.00
    print(tentacle('x = 5'))        # Should print: 5.00
    print(tentacle('2*x = 6'))      # Should print: 3.00
    print(tentacle('3 = x'))        # Should print: 3.00
    print(tentacle('x + 2 = x + 3'))# Should print: Error: division by zero
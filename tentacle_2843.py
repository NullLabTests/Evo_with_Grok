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
        
        # Extract coefficients a and b from the left side
        if 'x' in left_side:
            if left_side.startswith('-'):
                a = -1
                b_part = left_side[2:]  # Skip '-x'
            elif left_side.startswith('x'):
                a = 1
                b_part = left_side[1:]  # Skip 'x'
            else:
                a = float(left_side.split('x')[0])
                b_part = left_side.split('x')[1]
        else:
            a = 0
            b_part = left_side
        
        # Calculate b
        b = eval(b_part) if b_part else 0
        
        # Calculate c
        c = eval(right_side)
        
        # Solve for x
        x = (c - b) / a
        
        # Return the result as a string
        return str(x)
    
    except Exception as e:
        # Return an error message if solving fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('5*x - 2 = 8'))  # Should print: 2.0
    print(tentacle('-x + 4 = 1'))  # Should print: 3.0
    print(tentacle('x = 5'))  # Should print: 5.0
    print(tentacle('3*x = 9'))  # Should print: 3.0
    print(tentacle('2*x + 3 = x + 5'))  # Should print: 2.0
    print(tentacle('invalid equation'))  # Should print an error message
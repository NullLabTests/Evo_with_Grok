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
        equation = equation.replace(" ", "").split("=")
        if len(equation) != 2:
            raise ValueError("Invalid equation format")
        
        left, right = equation
        
        # Isolate the x term on the left side
        if 'x' in right:
            left, right = right, left
        
        # Parse the left side
        if 'x' not in left:
            raise ValueError("No x term found in the equation")
        
        if left == 'x':
            left_coefficient = 1
        elif left.startswith('-x'):
            left_coefficient = -1
        elif left.startswith('x'):
            left_coefficient = 1
        else:
            left_coefficient = float(left.split('x')[0])
        
        # Calculate the right side
        right_value = eval(right)
        
        # Solve for x
        x = (right_value - eval(left.replace('x', '0'))) / left_coefficient
        
        return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 10'))   # Should print: 15.0
    print(tentacle('-3*x = 9'))     # Should print: -3.0
    print(tentacle('2x = 8'))       # Should print: 4.0
    print(tentacle('x = 5'))        # Should print: 5.0
    print(tentacle('2*x + 3 = 3*x'))  # Should print: 3.0
    print(tentacle('invalid equation'))  # Should print an error message
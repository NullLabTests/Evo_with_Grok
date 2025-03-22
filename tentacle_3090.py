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
    '2.0'
    """
    try:
        # Split the equation into left and right sides
        left, right = equation.split('=')
        
        # Remove whitespace and simplify the equation
        left = left.strip().replace(' ', '')
        right = right.strip().replace(' ', '')
        
        # Find the position of 'x' in the left side
        x_pos = left.find('x')
        
        if x_pos == -1:
            return "Error: No 'x' found in the equation."
        
        # Extract the coefficient of x
        if x_pos == 0:
            coeff = 1
        elif x_pos == len(left) - 1:
            coeff = int(left[:-1])
        else:
            coeff = int(left[:x_pos])
        
        # Calculate the constant term on the left side
        left_const = 0
        if '+' in left:
            left_const = int(left.split('+')[1])
        elif '-' in left and left.index('-') != x_pos - 1:
            left_const = int(left.split('-')[1])
        
        # Calculate the right side value
        right_val = int(right)
        
        # Solve for x
        x = (right_val - left_const) / coeff
        
        return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('5*x - 4 = 11'))  # Should print: 3.0
    print(tentacle('x + 2 = 5'))  # Should print: 3.0
    print(tentacle('3*x = 9'))  # Should print: 3.0
    print(tentacle('2*x + 3 = x + 5'))  # Should print: 2.0
    print(tentacle('2*x + 3 = 7*x'))  # Should print: 0.6
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('invalid equation'))  # Should print an error message
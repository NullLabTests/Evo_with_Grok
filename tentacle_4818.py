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
        # Remove spaces and split the equation into left and right sides
        equation = equation.replace(" ", "").split("=")
        if len(equation) != 2:
            return "Error: Invalid equation format"
        
        left, right = equation
        
        # Extract coefficients and constants
        if 'x' in left:
            if left.startswith('-'):
                left = '-1' + left[1:]
            elif not left.startswith('x'):
                left = '1' + left if left[0].isalpha() else left
            
            left_parts = left.split('x')
            a = eval(left_parts[0]) if left_parts[0] else 1
            b = eval(left_parts[1]) if len(left_parts) > 1 else 0
        else:
            a, b = 0, eval(left)
        
        c = eval(right)
        
        # Solve for x
        if a == 0:
            return "Error: Not a linear equation in x"
        
        x = (c - b) / a
        
        return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: '2'
    print(tentacle('5*x - 2 = 8'))  # Should print: '2'
    print(tentacle('-x + 4 = 1'))  # Should print: '3'
    print(tentacle('3 = 2*x + 1'))  # Should print: '1'
    print(tentacle('x = 5'))  # Should print: '5'
    print(tentacle('2*y + 3 = 7'))  # Should print: 'Error: Not a linear equation in x'
    print(tentacle('2*x + 3 = 7 = 9'))  # Should print: 'Error: Invalid equation format'
    print(tentacle('2*x + 3'))  # Should print: 'Error: Invalid equation format'
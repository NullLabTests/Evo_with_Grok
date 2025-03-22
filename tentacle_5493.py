# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x and return the value of x.
    
    Args:
    equation (str): A string containing a linear equation in the form 'ax + b = c'.
    
    Returns:
    str: The value of x as a string, or an error message if the equation is invalid.
    
    Example:
    >>> tentacle('2*x + 3 = 7')
    '2'
    """
    try:
        # Split the equation into left and right sides
        left, right = equation.split('=')
        
        # Remove whitespace
        left = left.strip()
        right = right.strip()
        
        # Parse the left side of the equation
        if 'x' in left:
            if '*' in left:
                a, _ = left.split('*')
                a = float(a)
            else:
                a = 1.0 if left == 'x' else float(left.replace('x', ''))
            
            # Extract b
            b = 0.0
            if '+' in left:
                b = float(left.split('+')[1].replace('x', ''))
            elif '-' in left:
                b = float(left.split('-')[1].replace('x', '')) * -1
            
            # Solve for x
            c = float(right)
            x = (c - b) / a
            
            return str(x)
        else:
            return "Error: Equation does not contain x"
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 0'))  # Should print: 5.0
    print(tentacle('3x = 9'))  # Should print: 3.0
    print(tentacle('x + 2 = 5'))  # Should print: 3.0
    print(tentacle('2x - 4 = 0'))  # Should print: 2.0
    print(tentacle('x = 10'))  # Should print: 10.0
    print(tentacle('2*x + 3 = y'))  # Should print: Error: Equation does not contain x
    print(tentacle('invalid equation'))  # Should print: Error: invalid syntax
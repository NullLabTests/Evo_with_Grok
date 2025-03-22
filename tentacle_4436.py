# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.
    
    Args:
    equation (str): A string containing a linear equation in the form 'a*x + b = c'.
    
    Returns:
    str: The solution for x as a string, or an error message if the equation is invalid.
    
    Example:
    >>> tentacle('2*x + 3 = 7')
    '2'
    """
    try:
        # Split the equation into left and right sides
        left, right = equation.split('=')
        
        # Remove whitespace and simplify the equation
        left = left.strip().replace(' ', '')
        right = right.strip().replace(' ', '')
        
        # Extract coefficients
        if 'x' in left:
            a, b = left.split('+') if '+' in left else left.split('-')
            a = a.replace('x', '') if 'x' in a else '-' + a.replace('x', '')
            b = b if '+' in left else '-' + b
        else:
            a, b = '0', left
        
        a = float(a) if a else 1.0
        b = float(b) if b else 0.0
        c = float(right)
        
        # Solve for x
        x = (c - b) / a
        
        # Return the solution as a string
        return str(x)
    
    except Exception as e:
        # Return an error message if solving fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 0'))    # Should print: 5.0
    print(tentacle('3*x = 9'))      # Should print: 3.0
    print(tentacle('x + 2 = 2'))    # Should print: 0.0
    print(tentacle('2*x = x + 3'))  # Should print: 3.0
    print(tentacle('invalid'))      # Should print an error message
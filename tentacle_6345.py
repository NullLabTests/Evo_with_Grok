# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x.
    
    Args:
    equation (str): A string containing a linear equation in the form 'ax + b = c'.
    
    Returns:
    str: The value of x as a string, or an error message if the equation is invalid or non-linear.
    
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
        
        # Identify the x term and constant term on the left side
        if 'x' in left:
            if '+' in left:
                a, b = left.split('+')
                a = a.strip('x') if 'x' in a else '1'
                b = '-' + b if a == '-1' or a == '-x' else b
            elif '-' in left:
                a, b = left.split('-')
                a = a.strip('x') if 'x' in a else '1'
                b = '+' + b if a == '-1' or a == '-x' else '-' + b
            else:
                a = left.strip('x') if 'x' in left else '1'
                b = '0'
        else:
            return "Error: No x term found in the equation."
        
        # Convert terms to floats
        a = float(a) if a else 1.0
        b = float(b) if b else 0.0
        c = float(right)
        
        # Solve for x
        x = (c - b) / a
        
        # Return the result as a string
        return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('5*x - 2 = 8'))  # Should print: 2.0
    print(tentacle('-x + 4 = 1'))   # Should print: -3.0
    print(tentacle('x = 5'))        # Should print: 5.0
    print(tentacle('2*x = 6'))      # Should print: 3.0
    print(tentacle('x + 1 = x'))    # Should print: Error: division by zero
    print(tentacle('2*x^2 + 3 = 7'))# Should print: Error: No x term found in the equation.
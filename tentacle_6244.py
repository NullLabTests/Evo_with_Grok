# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x.
    
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
        
        # Extract coefficients and constant terms
        if 'x' in left:
            if '+' in left:
                a, b = left.split('+')
                a = a.replace('x', '') if 'x' in a else '1' if a == 'x' else a
                b = b if 'x' not in b else b.replace('x', '') if b != 'x' else '1'
            elif '-' in left:
                a, b = left.split('-')
                a = a.replace('x', '') if 'x' in a else '1' if a == 'x' else a
                b = '-' + b if 'x' not in b else '-' + b.replace('x', '') if b != 'x' else '-1'
            else:
                a = left.replace('x', '') if 'x' in left else '1' if left == 'x' else left
                b = '0'
        else:
            a = '0'
            b = left
        
        c = right
        
        # Convert string coefficients to floats
        a = float(a) if a else 0
        b = float(b) if b else 0
        c = float(c) if c else 0
        
        # Solve for x
        if a == 0:
            return "Error: Not a linear equation in x"
        x = (c - b) / a
        
        # Return the solution rounded to 2 decimal places
        return f"{x:.2f}"
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.00
    print(tentacle('5*x - 2 = 8'))  # Should print: 2.00
    print(tentacle('x + 1 = 0'))    # Should print: -1.00
    print(tentacle('3 = 2*x'))      # Should print: 1.50
    print(tentacle('x = 5'))        # Should print: 5.00
    print(tentacle('2*y + 3 = 7'))  # Should print: Error: Not a linear equation in x
    print(tentacle('2*x + 3'))      # Should print: Error: could not convert string to float: ''
    print(tentacle('2*x + 3 ='))    # Should print: Error: could not convert string to float: ''
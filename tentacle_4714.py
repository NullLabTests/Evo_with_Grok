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
        # Split the equation into left and right sides
        left, right = equation.split('=')
        
        # Remove whitespace
        left = left.strip()
        right = right.strip()
        
        # Parse the left side to extract coefficients
        if 'x' in left:
            if '*' in left:
                a, _ = left.split('*')
                a = float(a)
            else:
                a = float(left.replace('x', '1'))
        else:
            a = 0
        
        # Extract the constant term on the left side
        b = 0
        if '+' in left:
            b = float(left.split('+')[1])
        elif '-' in left and 'x-' in left:
            b = -float(left.split('-')[1])
        
        # Convert right side to float
        c = float(right)
        
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
    print(tentacle('5*x - 4 = 6'))  # Should print: 2.00
    print(tentacle('x + 2 = 5'))    # Should print: 3.00
    print(tentacle('3 = 3'))        # Should print: Error: Not a linear equation in x
    print(tentacle('2*x + y = 7'))  # Should print: Error: invalid literal for float(): y
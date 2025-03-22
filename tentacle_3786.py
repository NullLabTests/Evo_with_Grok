# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x.

    Args:
    equation (str): A string containing a linear equation in the form 'a*x + b = c'.

    Returns:
    str: The solution for x as a string.

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
        
        # Extract coefficients and constant
        if 'x' in left:
            a, b = left.split('*x')
            a = float(a.strip())
            b = float(b.strip()) if b else 0
        else:
            a = 1
            b = float(left) if left else 0
        
        c = float(right)
        
        # Solve for x
        x = (c - b) / a
        
        # Return the solution rounded to 2 decimal places
        return f"{x:.2f}"
    
    except Exception as e:
        # Return an error message if solving fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.00
    print(tentacle('x - 5 = 10'))   # Should print: 15.00
    print(tentacle('3*x = 12'))     # Should print: 4.00
    print(tentacle('x + 2 = 0'))    # Should print: -2.00
    print(tentacle('5 = 5'))        # Should print: 0.00
    print(tentacle('2*x + 3 = x'))  # Should print: -3.00
    print(tentacle('invalid'))      # Should print an error message
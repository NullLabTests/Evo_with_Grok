# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.
    
    Args:
    equation (str): A string containing a linear equation in the form 'a*x + b = c'.
    
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
        
        # Parse the left side of the equation
        if '*' in left:
            a, rest = left.split('*')
            a = float(a.strip())
            b = float(rest.replace('x', '0'))
        else:
            a = float(left.replace('x', '1'))
            b = 0
        
        # Calculate x
        c = float(right)
        x = (c - b) / a
        
        # Return the solution rounded to 2 decimal places
        return f"{x:.2f}"
    
    except Exception as e:
        # Return an error message if solving fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.00
    print(tentacle('5*x - 2 = 8'))  # Should print: 2.00
    print(tentacle('x + 4 = 10'))   # Should print: 6.00
    print(tentacle('3*x = 15'))     # Should print: 5.00
    print(tentacle('2*x + 3 = x'))  # Should print: -3.00
    print(tentacle('invalid'))      # Should print an error message
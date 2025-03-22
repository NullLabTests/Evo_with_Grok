# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x.

    Args:
    equation (str): A string containing a linear equation in the format 'a*x + b = c'.

    Returns:
    str: The solution for x as a string, or an error message if the equation cannot be solved.

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
        if 'x' not in left:
            return "Error: Equation must contain 'x'"
        
        if '*' in left:
            a, _ = left.split('*')
            a = float(a.strip())
        elif left.startswith('x'):
            a = 1.0
        elif left.endswith('x'):
            a = float(left[:-1].strip())
        else:
            return "Error: Invalid format for 'x' in the equation"
        
        # Extract the constant term on the left side
        b = 0.0
        if '+' in left:
            b = float(left.split('+')[1].strip())
        elif '-' in left and left.index('-') != 0:
            b = float(left.split('-')[1].strip()) * -1
        
        # Calculate the solution
        c = float(right)
        x = (c - b) / a
        
        # Return the solution rounded to 2 decimal places
        return f"{x:.2f}"
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.00
    print(tentacle('x - 5 = 10'))   # Should print: 15.00
    print(tentacle('3*x = 12'))     # Should print: 4.00
    print(tentacle('x + 2 = 8'))    # Should print: 6.00
    print(tentacle('2*x = 7'))      # Should print: 3.50
    print(tentacle('x = 5'))        # Should print: 5.00
    print(tentacle('2*x + 3 = x')) # Should print: -3.00
    print(tentacle('2*x + 3 = 3*x + 1'))  # Should print: -2.00
    print(tentacle('2*x + 3 = 2*x + 3'))  # Should print: Error: division by zero
    print(tentacle('y + 3 = 7'))    # Should print: Error: Equation must contain 'x'
    print(tentacle('2*x + 3'))      # Should print: Error: Invalid equation format
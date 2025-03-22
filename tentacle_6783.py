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
        
        # Extract coefficients
        if 'x' in left:
            a, b = left.split('*x')
            a = float(a.strip()) if a.strip() else 1.0
            b = float(b.strip()) if b.strip() else 0.0
        else:
            a = 0.0
            b = float(left)
        
        c = float(right)
        
        # Solve for x
        if a == 0:
            if b == c:
                return 'Infinite solutions (all real numbers)'
            else:
                return 'No solution'
        else:
            x = (c - b) / a
            return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x + 5 = 10'))   # Should print: 5.0
    print(tentacle('3*x = 9'))      # Should print: 3.0
    print(tentacle('5 = 5'))        # Should print: Infinite solutions (all real numbers)
    print(tentacle('5 = 6'))        # Should print: No solution
    print(tentacle('2*x + 3 = y'))  # Should print: Error: could not convert string to float: 'y'
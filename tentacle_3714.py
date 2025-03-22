# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x.

    Args:
    equation (str): A string containing a linear equation in the form 'ax + b = c'.

    Returns:
    str: The solution for x as a string.

    Example:
    >>> tentacle('2*x + 3 = 7')
    '2'
    """
    try:
        # Remove spaces and split the equation at the equals sign
        left, right = equation.replace(" ", "").split("=")
        
        # Parse the left side of the equation
        if 'x' in left:
            if left.startswith('x'):
                a = 1
                b = 0 if len(left) == 1 else float(left[1:])
            elif left.endswith('x'):
                a = float(left[:-1])
                b = 0
            else:
                a, b = map(float, left.split('x'))
        else:
            a = 0
            b = float(left)
        
        # Parse the right side of the equation
        c = float(right)
        
        # Solve for x
        if a == 0:
            if b == c:
                return 'All real numbers'
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
    print(tentacle('5 = 5'))        # Should print: All real numbers
    print(tentacle('5 = 6'))        # Should print: No solution
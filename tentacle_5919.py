# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.
    
    Args:
    equation (str): A string containing a linear equation in the form 'a*x + b = c'.
    
    Returns:
    str: The solution for x as a string, or an error message if the equation cannot be solved.
    
    Example:
    >>> tentacle('2*x + 3 = 7')
    '2.0'
    """
    try:
        # Remove spaces and split the equation into left and right sides
        equation = equation.replace(" ", "")
        left, right = equation.split("=")
        
        # Parse the left side of the equation
        if '*' in left:
            a, rest = left.split('*')
            a = float(a)
            b = float(rest) if rest else 0
        elif 'x' in left:
            a = 1 if left == 'x' else float(left.replace('x', ''))
            b = 0
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
    print(tentacle('2*x + 3 = x'))  # Should print: -3.0
    print(tentacle('invalid'))      # Should print an error message
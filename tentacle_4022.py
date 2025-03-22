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
        import re
        x_term = re.search(r'([+-]?\d*\.?\d*)?\*?x', left)
        constant_term = re.sub(r'([+-]?\d*\.?\d*)?\*?x', '', left)
        
        a = float(x_term.group(1)) if x_term.group(1) else 1  # Coefficient of x
        b = float(constant_term) if constant_term else 0  # Constant term
        
        # Calculate x
        c = float(right)
        x = (c - b) / a
        
        # Return the solution rounded to 2 decimal places
        return f"{x:.2f}"
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.00
    print(tentacle('x - 5 = 10'))  # Should print: 15.00
    print(tentacle('3*x = 9'))  # Should print: 3.00
    print(tentacle('2*x + 3 = x + 7'))  # Should print: 4.00
    print(tentacle('invalid equation'))  # Should print an error message
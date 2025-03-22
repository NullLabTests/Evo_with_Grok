# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.
    
    Args:
    equation (str): A string containing a linear equation in the form 'a*x + b = c'.
    
    Returns:
    str: The solution for x as a string.
    
    Example:
    >>> tentacle('2*x + 3 = 7')
    '2'
    """
    import re
    
    # Remove spaces and convert to lowercase
    equation = equation.replace(" ", "").lower()
    
    # Extract coefficients and constant using regex
    match = re.match(r"(\-?\d*\.?\d*)?\*?x(\+|-)(\-?\d*\.?\d*)=(\-?\d*\.?\d*)", equation)
    if not match:
        return "Error: Invalid equation format"
    
    a, sign, b, c = match.groups()
    
    # Convert coefficients to floats
    a = float(a) if a and a != '-' else -1 if a == '-' else 1
    b = float(b) if b else 0
    c = float(c)
    
    # Adjust b based on the sign
    b = b if sign == '+' else -b
    
    # Solve for x
    if a == 0:
        return "Error: 'a' cannot be zero in a*x + b = c"
    
    x = (c - b) / a
    
    return str(x)

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 0'))  # Should print: 5.0
    print(tentacle('-3*x + 2 = -10'))  # Should print: 4.0
    print(tentacle('0*x + 3 = 7'))  # Should print: Error: 'a' cannot be zero in a*x + b = c
    print(tentacle('2*y + 3 = 7'))  # Should print: Error: Invalid equation format
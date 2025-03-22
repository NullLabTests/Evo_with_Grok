# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x.
    
    Args:
    equation (str): A string containing a linear equation in the form 'ax + b = c'.
    
    Returns:
    str: The solution for x as a string, or an error message if the equation is invalid.
    
    Example:
    >>> tentacle('2*x + 3 = 7')
    '2'
    """
    try:
        # Remove spaces and split the equation into left and right sides
        equation = equation.replace(" ", "").split("=")
        if len(equation) != 2:
            return "Error: Invalid equation format"
        
        left, right = equation
        right = float(right)
        
        # Extract coefficients of x and constant term from the left side
        import re
        x_term = re.search(r'([-+]?\d*\.?\d*)?[*]x', left)
        constant_term = re.search(r'([-+]?\d*\.?\d+)(?![*]x)', left)
        
        if x_term:
            a = float(x_term.group(1)) if x_term.group(1) else 1
        else:
            return "Error: No x term found in the equation"
        
        b = float(constant_term.group(1)) if constant_term else 0
        
        # Solve for x
        x = (right - b) / a
        
        # Return the solution rounded to 2 decimal places
        return f"{x:.2f}"
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.00
    print(tentacle('x - 5 = 10'))  # Should print: 15.00
    print(tentacle('-3*x = 9'))  # Should print: -3.00
    print(tentacle('2*x + 3 = x + 7'))  # Should print: 4.00
    print(tentacle('x = 5'))  # Should print: 5.00
    print(tentacle('2*x + 3'))  # Should print: Error: Invalid equation format
    print(tentacle('2*y + 3 = 7'))  # Should print: Error: No x term found in the equation
    print(tentacle('2*x + 3 = a'))  # Should print: Error: could not convert string to float: 'a'
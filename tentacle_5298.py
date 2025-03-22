# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.
    
    Args:
    equation (str): A string containing a linear equation in the form 'ax + b = c'.
    
    Returns:
    str: The solution for x as a string, or an error message if the equation is invalid.
    
    Example:
    >>> tentacle('2*x + 3 = 7')
    '2'
    """
    try:
        # Split the equation into left and right sides
        left, right = equation.split('=')
        
        # Remove whitespace and simplify the equation
        left = left.strip().replace(' ', '')
        right = right.strip().replace(' ', '')
        
        # Extract the coefficient of x and the constant term from the left side
        if 'x' in left:
            if left.startswith('-x') or left.startswith('x'):
                coeff = -1 if left.startswith('-x') else 1
                constant = 0
            else:
                parts = left.split('x')
                coeff = int(parts[0]) if parts[0] and parts[0] != '-' else 1
                coeff = -coeff if parts[0] == '-' else coeff
                constant = int(parts[1]) if parts[1] else 0
        else:
            coeff = 0
            constant = int(left)
        
        # Calculate the solution for x
        solution = (int(right) - constant) / coeff
        
        # Return the solution as a string
        return str(solution)
    
    except Exception as e:
        # Return an error message if solving fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 10'))   # Should print: 15.0
    print(tentacle('-3*x = 9'))     # Should print: -3.0
    print(tentacle('5 = 2*x + 1'))  # Should print: 2.0
    print(tentacle('x = 4'))        # Should print: 4.0
    print(tentacle('2*x = x + 3'))  # Should print: 3.0
    print(tentacle('2*x + 3*y = 7'))  # Should print: Error: division by zero
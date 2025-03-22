# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.
    
    Args:
    equation (str): A string containing a linear equation in the form 'ax + b = c'.
    
    Returns:
    str: The solution for x as a string.
    
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
        
        # Identify the coefficient of x and constant on the left side
        if 'x' in left:
            if left.startswith('-x') or left.startswith('x'):
                coeff = -1 if left.startswith('-x') else 1
                const_left = 0
            else:
                parts = left.split('+')
                coeff_part = [p for p in parts if 'x' in p][0]
                coeff = float(coeff_part.replace('x', '')) if coeff_part != 'x' else 1
                const_left = sum(float(p) for p in parts if 'x' not in p)
        else:
            coeff = 0
            const_left = float(left)
        
        # Calculate the constant on the right side
        const_right = float(right)
        
        # Solve for x
        if coeff == 0:
            if const_left == const_right:
                return 'Infinite solutions (0 = 0)'
            else:
                return 'No solution'
        else:
            x = (const_right - const_left) / coeff
            return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 0'))    # Should print: 5.0
    print(tentacle('3*x = 9'))      # Should print: 3.0
    print(tentacle('0 = 0'))        # Should print: Infinite solutions (0 = 0)
    print(tentacle('1 = 2'))        # Should print: No solution
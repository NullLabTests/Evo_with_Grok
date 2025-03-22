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
        
        # Remove whitespace
        left = left.strip()
        right = right.strip()
        
        # Extract the coefficient of x and the constant term from the left side
        if 'x' in left:
            if '*' in left:
                coef, const = left.split('*')
                coef = coef.strip()
                const = const.replace('x', '').strip()
            else:
                coef = '1'
                const = left.replace('x', '').strip()
        else:
            coef = '0'
            const = left.strip()
        
        # Convert string values to floats
        coef = float(coef) if coef else 0
        const = float(const) if const else 0
        right = float(right)
        
        # Solve for x
        if coef == 0:
            if const == right:
                return 'Infinite solutions (any x)'
            else:
                return 'No solution'
        else:
            x = (right - const) / coef
            return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 0'))  # Should print: 5.0
    print(tentacle('3*x = 9'))  # Should print: 3.0
    print(tentacle('0*x + 2 = 2'))  # Should print: Infinite solutions (any x)
    print(tentacle('0*x + 2 = 3'))  # Should print: No solution
    print(tentacle('invalid equation'))  # Should print: Error: ...
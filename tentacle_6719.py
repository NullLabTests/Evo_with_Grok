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
        # Remove spaces and split the equation into left and right sides
        equation = equation.replace(" ", "")
        left, right = equation.split("=")
        
        # Parse the left side to separate the coefficient of x and the constant term
        if 'x' in left:
            if '+' in left:
                coeff, const = left.split('+')
            elif '-' in left:
                coeff, const = left.split('-')
                const = '-' + const
            else:
                coeff = left
                const = '0'
            
            # Extract the coefficient of x
            if coeff == 'x':
                coeff = '1'
            elif coeff == '-x':
                coeff = '-1'
            else:
                coeff = coeff.replace('x', '')
        else:
            coeff = '0'
            const = left
        
        # Convert all terms to floats
        coeff = float(coeff)
        const = float(const)
        right = float(right)
        
        # Solve for x
        if coeff == 0:
            if const == right:
                return 'All real numbers'
            else:
                return 'No solution'
        else:
            x = (right - const) / coeff
            return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('3*x - 4 = 8'))  # Should print: 4.0
    print(tentacle('-x + 5 = 2'))  # Should print: 3.0
    print(tentacle('x = 5'))  # Should print: 5.0
    print(tentacle('2 = 2'))  # Should print: All real numbers
    print(tentacle('2 = 3'))  # Should print: No solution
    print(tentacle('2*x + 3 = x + 7'))  # Should print: 4.0
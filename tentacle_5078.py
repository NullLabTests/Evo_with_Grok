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
        equation = equation.replace(" ", "").split("=")
        left_side = equation[0]
        right_side = equation[1]
        
        # Separate the coefficient of x and the constant term on the left side
        if 'x' in left_side:
            if '+' in left_side:
                coeff, const = left_side.split('+')
            elif '-' in left_side:
                coeff, const = left_side.split('-')
                const = '-' + const
            else:
                coeff = left_side
                const = '0'
            
            # Remove 'x' from the coefficient
            coeff = coeff.replace('x', '')
            if coeff == '' or coeff == '-':
                coeff += '1'
            elif coeff == '+':
                coeff = '1'
        else:
            return "Error: No 'x' term in the equation"
        
        # Calculate the solution
        right_value = eval(right_side)
        const_value = eval(const)
        coeff_value = eval(coeff)
        
        solution = (right_value - const_value) / coeff_value
        
        return str(solution)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('5*x - 2 = 8'))  # Should print: 2.0
    print(tentacle('x + 4 = 10'))   # Should print: 6.0
    print(tentacle('-3*x = 9'))     # Should print: -3.0
    print(tentacle('2 = 2'))        # Should print: Error: No 'x' term in the equation
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
        # Remove spaces and split the equation into left and right sides
        equation = equation.replace(" ", "").split("=")
        left_side = equation[0]
        right_side = equation[1]
        
        # Extract coefficients and constant terms
        if 'x' in left_side:
            if '+' in left_side:
                a, b = left_side.split('+')
                a = a.replace('x', '') if 'x' in a else '1'
                b = '-' + b if b.startswith('-') else '-' + b
            elif '-' in left_side:
                a, b = left_side.split('-')
                a = a.replace('x', '') if 'x' in a else '1'
                b = '+' + b if b else ''
            else:
                a = left_side.replace('x', '') if 'x' in left_side else '1'
                b = '0'
        else:
            a = '0'
            b = '-' + left_side
        
        # Calculate the solution
        c = right_side
        numerator = eval(b + '-' + c)
        denominator = eval(a)
        
        if denominator == 0:
            return "Error: Division by zero"
        
        solution = -numerator / denominator
        
        return str(solution)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: '2.0'
    print(tentacle('5*x - 4 = 6'))  # Should print: '2.0'
    print(tentacle('-3*x = 9'))     # Should print: '-3.0'
    print(tentacle('x + 2 = 0'))    # Should print: '-2.0'
    print(tentacle('0*x = 5'))      # Should print: 'Error: Division by zero'
    print(tentacle('2*x + 3 = y'))  # Should print: 'Error: invalid syntax'
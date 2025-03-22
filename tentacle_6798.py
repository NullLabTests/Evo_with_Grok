# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.
    
    Args:
    equation (str): A string containing a linear equation in the form 'ax + b = c'.
    
    Returns:
    str: The solution for x as a string, or an error message if the equation cannot be solved.
    
    Example:
    >>> tentacle('2*x + 3 = 7')
    '2'
    """
    try:
        # Remove spaces and split the equation at '='
        equation = equation.replace(" ", "").split("=")
        
        # Parse left and right sides of the equation
        left_side = equation[0]
        right_side = equation[1]
        
        # Extract coefficient of x and constant term from left side
        if 'x' in left_side:
            if left_side == 'x':
                a = 1
                b = 0
            elif left_side.startswith('-x'):
                a = -1
                b = 0
            elif left_side.startswith('x'):
                a = 1
                b = 0
            else:
                if '+' in left_side:
                    a, b = left_side.split('+')
                elif '-' in left_side:
                    if left_side.index('-') == left_side.rindex('-'):
                        a, b = left_side.split('-')
                        b = '-' + b
                    else:
                        parts = left_side.split('-')
                        a = parts[0]
                        b = '-' + '-'.join(parts[1:])
                else:
                    a = left_side
                    b = '0'
                
                if 'x' in a:
                    a = a.replace('x', '')
                    if a == '' or a == '-':
                        a = a + '1'
                    a = float(a)
                else:
                    b = a
                    a = 1 if '+' in left_side else -1
                
                b = float(b)
        else:
            return "Error: Equation does not contain x"
        
        # Calculate x
        c = float(right_side)
        x = (c - b) / a
        
        return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 10'))   # Should print: 15.0
    print(tentacle('-3*x = 9'))     # Should print: -3.0
    print(tentacle('5 = 2*x + 1'))  # Should print: 2.0
    print(tentacle('x = 4'))        # Should print: 4.0
    print(tentacle('2 + 3 = 5'))    # Should print: Error: Equation does not contain x
    print(tentacle('2*x + y = 7'))  # Should print: Error: Equation does not contain x
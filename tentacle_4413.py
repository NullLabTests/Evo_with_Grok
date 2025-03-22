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
        # Remove whitespace and split the equation into left and right sides
        equation = equation.replace(" ", "").split("=")
        if len(equation) != 2:
            return "Error: Invalid equation format"
        
        left_side, right_side = equation
        
        # Parse the left side to extract the coefficient of x and the constant term
        if 'x' not in left_side:
            return "Error: No 'x' term in the equation"
        
        if left_side == 'x':
            x_coefficient = 1
            constant_term = 0
        elif left_side.startswith('-x'):
            x_coefficient = -1
            constant_term = 0
        else:
            if '+' in left_side:
                terms = left_side.split('+')
            elif '-' in left_side:
                terms = left_side.split('-')
                terms[1:] = ['-' + term for term in terms[1:]]
            else:
                terms = [left_side]
            
            x_coefficient = 0
            constant_term = 0
            
            for term in terms:
                if 'x' in term:
                    if term == 'x':
                        x_coefficient += 1
                    elif term == '-x':
                        x_coefficient -= 1
                    else:
                        x_coefficient += float(term.replace('x', ''))
                else:
                    constant_term += float(term)
        
        # Calculate the solution for x
        right_value = float(right_side)
        x = (right_value - constant_term) / x_coefficient
        
        # Return the solution as a string
        return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('5*x - 2 = 13'))  # Should print: 3.0
    print(tentacle('-x + 4 = 1'))  # Should print: 3.0
    print(tentacle('x = 5'))  # Should print: 5.0
    print(tentacle('2*x = 10'))  # Should print: 5.0
    print(tentacle('3*x + 2*x - 5 = 10'))  # Should print: 3.0
    print(tentacle('invalid equation'))  # Should print an error message
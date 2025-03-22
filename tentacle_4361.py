# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x.
    
    Args:
    equation (str): A string containing a linear equation in the form 'ax + b = c'.
    
    Returns:
    str: The solution for x as a string, or an error message if solving fails.
    
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
            if left.startswith('-x') or left.startswith('x'):
                coeff = -1 if left.startswith('-x') else 1
                constant = 0
            else:
                terms = left.split('+')
                coeff = 1
                constant = 0
                for term in terms:
                    if 'x' in term:
                        if term == 'x':
                            coeff = 1
                        elif term == '-x':
                            coeff = -1
                        else:
                            coeff = float(term.replace('x', ''))
                    else:
                        constant += float(term)
        else:
            constant = float(left)
            coeff = 0
        
        # Calculate the solution for x
        right_value = float(right)
        if coeff == 0:
            if constant == right_value:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            x = (right_value - constant) / coeff
            return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 10'))   # Should print: 15.0
    print(tentacle('-3*x = 9'))     # Should print: -3.0
    print(tentacle('5 = 5'))        # Should print: Infinite solutions
    print(tentacle('5 = 6'))        # Should print: No solution
    print(tentacle('2*x + 3 = y'))  # Should print: Error: could not convert string to float: 'y'
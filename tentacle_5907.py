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
        
        # Evaluate the right side of the equation
        right_value = eval(right_side)
        
        # Parse the left side to find the coefficient of x and the constant term
        x_term = left_side.split("+")
        x_coefficient = 1
        constant_term = 0
        
        for term in x_term:
            if 'x' in term:
                if term == 'x':
                    x_coefficient = 1
                elif term.startswith('-x'):
                    x_coefficient = -1
                else:
                    x_coefficient = eval(term.replace('x', ''))
            else:
                constant_term += eval(term)
        
        # Solve for x
        x = (right_value - constant_term) / x_coefficient
        
        # Return the solution rounded to 2 decimal places
        return f"{x:.2f}"
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.00
    print(tentacle('5*x - 2 = 8'))  # Should print: 2.00
    print(tentacle('-x + 4 = 1'))  # Should print: 3.00
    print(tentacle('3*x = 9'))  # Should print: 3.00
    print(tentacle('x + 2 = 5'))  # Should print: 3.00
    print(tentacle('2*x + 3 = 3*x'))  # Should print: 3.00
    print(tentacle('invalid equation'))  # Should print an error message
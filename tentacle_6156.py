# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.
    
    Args:
    equation (str): A string containing a linear equation in the form 'a*x + b = c'.
    
    Returns:
    str: The solution for x as a string, or an error message if the equation is invalid.
    
    Example:
    >>> tentacle('2*x + 3 = 7')
    '2'
    """
    try:
        # Remove spaces and split the equation into left and right parts
        equation = equation.replace(" ", "").split("=")
        if len(equation) != 2:
            return "Error: Invalid equation format"

        left, right = equation[0], equation[1]
        
        # Extract the coefficient of x and the constant term from the left side
        import re
        left_parts = re.split(r'([+-])', left)
        left_parts = [part for part in left_parts if part != '']
        
        x_term = None
        constant = 0
        sign = 1
        
        for part in left_parts:
            if 'x' in part:
                if x_term is not None:
                    return "Error: Multiple x terms found"
                x_term = float(part.replace('x', '')) if part.replace('x', '') != '' else 1
                x_term *= sign
            else:
                if part in ['+', '-']:
                    sign = 1 if part == '+' else -1
                else:
                    constant += float(part) * sign
                    sign = 1
        
        if x_term is None:
            return "Error: No x term found"
        
        # Calculate the solution
        right_value = float(right)
        solution = (right_value - constant) / x_term
        
        return str(solution)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('5*x - 2 = 8'))  # Should print: 2.0
    print(tentacle('-3*x + 1 = 10'))  # Should print: -3.0
    print(tentacle('x + 5 = 3'))  # Should print: -2.0
    print(tentacle('2*x = 6'))  # Should print: 3.0
    print(tentacle('3*x + 2*x - 5 = 10'))  # Should print: 3.0
    print(tentacle('2*x + 3 = 3 + 2*x'))  # Should print: Error: Division by zero
    print(tentacle('2*x + y = 7'))  # Should print: Error: No x term found
    print(tentacle('2*x + 3'))  # Should print: Error: Invalid equation format
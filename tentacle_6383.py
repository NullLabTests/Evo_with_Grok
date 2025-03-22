# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve the equation for x given as a string.
    
    Args:
    equation (str): A string containing a linear equation in the form 'ax + b = c'.
    
    Returns:
    str: The solution for x as a string.
    
    Example:
    >>> tentacle('2*x + 3 = 7')
    '2'
    """
    try:
        # Remove whitespace and split the equation into left and right sides
        equation = equation.replace(" ", "").split("=")
        left_side = equation[0]
        right_side = equation[1]
        
        # Parse the left side to extract the coefficient of x and the constant term
        if 'x' in left_side:
            if '+' in left_side:
                a, b = left_side.split('+')
            elif '-' in left_side:
                a, b = left_side.split('-')
                b = '-' + b
            else:
                a = left_side
                b = '0'
            
            # Extract the coefficient of x
            if a == 'x':
                a = '1'
            elif a == '-x':
                a = '-1'
            else:
                a = a.replace('x', '')
            
            # Convert a and b to floats
            a = float(a)
            b = float(b)
        else:
            return "Error: Equation does not contain x"
        
        # Evaluate the right side
        c = float(eval(right_side))
        
        # Solve for x
        x = (c - b) / a
        
        # Return the solution rounded to 2 decimal places
        return f"{x:.2f}"
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.00
    print(tentacle('5*x - 10 = 0'))  # Should print: 2.00
    print(tentacle('-3*x + 4 = 1'))  # Should print: 1.00
    print(tentacle('x + 2 = 5'))    # Should print: 3.00
    print(tentacle('2 = 2'))        # Should print: Error: Equation does not contain x
    print(tentacle('2*x + y = 7'))  # Should print: Error: Equation does not contain x
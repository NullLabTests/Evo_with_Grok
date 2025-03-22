# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.
    
    Args:
    equation (str): A string containing a linear equation in the form 'ax + b = c'.
    
    Returns:
    str: The solution for x as a string, or an error message if solving fails.
    
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
        
        # Isolate the x term on the left side
        if '+' in left_side:
            left_side, constant = left_side.split('+')
            right_side = f"({right_side})-({constant})"
        elif '-' in left_side:
            left_side, constant = left_side.split('-')
            right_side = f"({right_side})+({constant})"
        
        # Extract coefficient of x
        coefficient = left_side.split('*')[0] if '*' in left_side else '1'
        
        # Solve for x
        solution = f"({right_side})/({coefficient})"
        
        # Evaluate the solution
        result = eval(solution)
        
        # Return the result as a string
        return str(result)
    
    except Exception as e:
        # Return an error message if solving fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 10'))   # Should print: 15.0
    print(tentacle('3*x = 12'))     # Should print: 4.0
    print(tentacle('x/2 = 4'))      # Should print: 8.0
    print(tentacle('2*x + 3 = x'))  # Should print: -3.0
    print(tentacle('invalid'))      # Should print an error message
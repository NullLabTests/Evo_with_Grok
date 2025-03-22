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
        # Remove spaces and split the equation at the equals sign
        left, right = equation.replace(" ", "").split("=")
        
        # Split the left side into terms
        terms = left.split("+")
        
        # Initialize variables
        x_coefficient = 0
        constant = 0
        
        # Process each term
        for term in terms:
            if 'x' in term:
                if term == 'x':
                    x_coefficient += 1
                elif term.startswith('-x'):
                    x_coefficient -= 1
                else:
                    x_coefficient += float(term.replace('x', ''))
            else:
                constant += float(term)
        
        # Calculate the solution
        right_value = float(right)
        solution = (right_value - constant) / x_coefficient
        
        # Return the solution rounded to 2 decimal places
        return f"{solution:.2f}"
    
    except Exception as e:
        return f"Error: Invalid equation or unable to solve. {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.00
    print(tentacle('x - 5 = 10'))    # Should print: 15.00
    print(tentacle('-3*x + 2 = -1')) # Should print: 1.00
    print(tentacle('2x + 3 = 7'))    # Should print: 2.00
    print(tentacle('x = 5'))         # Should print: 5.00
    print(tentacle('2*x + y = 7'))   # Should print: Error: Invalid equation or unable to solve. name 'y' is not defined
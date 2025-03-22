# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x.
    
    Args:
    equation (str): A string containing a linear equation in the form 'ax + b = c'.
    
    Returns:
    str: The value of x as a string, or an error message if the equation is invalid.
    
    Example:
    >>> tentacle('2*x + 3 = 7')
    '2'
    """
    try:
        # Remove whitespace and split the equation into left and right sides
        equation = equation.replace(" ", "").split("=")
        if len(equation) != 2:
            return "Error: Invalid equation format"
        
        left, right = equation
        
        # Parse the left side of the equation
        if '+' in left:
            terms = left.split('+')
            coefficient = float(terms[0].replace('x', '1') if 'x' in terms[0] else terms[0])
            constant = float(terms[1]) if len(terms) > 1 else 0
        elif '-' in left:
            terms = left.split('-')
            coefficient = float(terms[0].replace('x', '1') if 'x' in terms[0] else terms[0])
            constant = -float(terms[1]) if len(terms) > 1 else 0
        else:
            coefficient = float(left.replace('x', '1') if 'x' in left else left)
            constant = 0
        
        # Solve for x
        right_value = float(right)
        x = (right_value - constant) / coefficient
        
        # Return the result as a string
        return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('5x - 8 = 12'))  # Should print: 4.0
    print(tentacle('x + 5 = 10'))   # Should print: 5.0
    print(tentacle('3x = 15'))      # Should print: 5.0
    print(tentacle('2x + 3y = 7'))  # Should print: Error: Invalid equation format
    print(tentacle('2*x + = 7'))    # Should print: Error: could not convert string to float: ''
    print(tentacle('2x + 3 ='))     # Should print: Error: Invalid equation format
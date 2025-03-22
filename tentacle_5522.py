# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.
    
    Args:
    equation (str): A string containing a linear equation in the form 'ax + b = c'.
    
    Returns:
    str: The solution for x as a string, or an error message if the equation is invalid.
    
    Example:
    >>> tentacle('2*x + 3 = 7')
    '2'
    """
    try:
        # Split the equation into left and right sides
        left, right = equation.split('=')
        
        # Remove whitespace
        left = left.strip()
        right = right.strip()
        
        # Parse the left side
        if 'x' not in left:
            return "Error: Equation must contain 'x'"
        
        # Split left side into terms
        terms = left.split('+')
        x_term = None
        constant_term = 0
        
        for term in terms:
            term = term.strip()
            if 'x' in term:
                if x_term is not None:
                    return "Error: Only one x term is allowed"
                x_term = term.replace('x', '').strip()
                if x_term == '' or x_term == '-':
                    x_term += '1'
                x_term = float(x_term)
            else:
                constant_term += float(term)
        
        # Solve for x
        right_value = float(right)
        if x_term == 0:
            return "Error: Coefficient of x cannot be zero"
        
        x = (right_value - constant_term) / x_term
        
        return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 10'))  # Should print: 15.0
    print(tentacle('-3*x + 2 = -1'))  # Should print: 1.0
    print(tentacle('2*x = 6'))  # Should print: 3.0
    print(tentacle('x + 1 = 1'))  # Should print: 0.0
    print(tentacle('2*x + 3 = 3*x'))  # Should print: 3.0
    print(tentacle('x = 5'))  # Should print: 5.0
    print(tentacle('2*x + 3 = 3'))  # Should print: 0.0
    print(tentacle('2*x + y = 7'))  # Should print: Error: Equation must contain 'x'
    print(tentacle('2*x + 3 ='))  # Should print: Error: could not convert string to float: ''
    print(tentacle('2*x + 3*x = 7'))  # Should print: Error: Only one x term is allowed
    print(tentacle('0*x + 3 = 7'))  # Should print: Error: Coefficient of x cannot be zero
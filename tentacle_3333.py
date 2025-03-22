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
        
        # Parse the left side to extract coefficients
        terms = left.split('+')
        x_coefficient = 0
        constant = 0
        
        for term in terms:
            term = term.strip()
            if 'x' in term:
                if term == 'x':
                    x_coefficient += 1
                elif term.startswith('-x'):
                    x_coefficient -= 1
                else:
                    x_coefficient += float(term.replace('x', ''))
            else:
                constant += float(term)
        
        # Calculate x
        right_value = float(right)
        x = (right_value - constant) / x_coefficient
        
        # Return the solution rounded to 2 decimal places
        return f"{x:.2f}"
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.00
    print(tentacle('5*x - 4 = 6'))  # Should print: 2.00
    print(tentacle('x + 2 = 5'))    # Should print: 3.00
    print(tentacle('3*x = 9'))      # Should print: 3.00
    print(tentacle('2*x + 3 = x + 5'))  # Should print: 2.00
    print(tentacle('invalid equation')) # Should print an error message
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
        # Split the equation into left and right sides
        left, right = equation.split('=')
        
        # Remove whitespace
        left, right = left.strip(), right.strip()
        
        # Parse the left side to extract coefficients
        terms = left.split('+')
        a = 0
        b = 0
        for term in terms:
            term = term.strip()
            if 'x' in term:
                if term == 'x':
                    a += 1
                elif term.startswith('-x'):
                    a -= 1
                else:
                    a += float(term.replace('x', ''))
            else:
                b += float(term)
        
        # Parse the right side
        c = float(right)
        
        # Solve for x
        x = (c - b) / a
        
        # Return the solution rounded to 2 decimal places
        return f"{x:.2f}"
    
    except Exception as e:
        # Return an error message if solving fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.00
    print(tentacle('5*x - 2 = 8'))  # Should print: 2.00
    print(tentacle('-3*x + 1 = -5'))  # Should print: 2.00
    print(tentacle('x + 4 = 6'))  # Should print: 2.00
    print(tentacle('2*x = 4'))  # Should print: 2.00
    print(tentacle('invalid equation'))  # Should print an error message
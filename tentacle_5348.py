# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x.

    Args:
    equation (str): A string containing a linear equation in the format 'a*x + b = c'.

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
        if a == 0:
            return "Error: Coefficient of x cannot be zero"
        
        x = (c - b) / a
        
        return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('5*x - 2 = 8'))  # Should print: 2.0
    print(tentacle('x + 1 = 0'))    # Should print: -1.0
    print(tentacle('2*x = 6'))      # Should print: 3.0
    print(tentacle('3 = 3'))        # Should print: Error: Equation must contain 'x'
    print(tentacle('0*x + 1 = 2'))  # Should print: Error: Coefficient of x cannot be zero
    print(tentacle('x + y = 3'))    # Should print: Error: Equation must contain 'x'
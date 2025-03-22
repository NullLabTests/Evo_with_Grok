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
        if 'x' not in left:
            return "Error: Equation does not contain x"
        
        # Split left side into terms
        terms = left.split('+')
        a = 0
        b = 0
        
        for term in terms:
            term = term.strip()
            if term == 'x':
                a += 1
            elif term.endswith('x'):
                a += float(term[:-1])
            else:
                b += float(term)
        
        # Parse the right side
        c = float(right)
        
        # Solve for x
        if a == 0:
            return "Error: Coefficient of x is zero"
        
        x = (c - b) / a
        
        return str(x)
    
    except ValueError:
        return "Error: Invalid equation format"
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x + 5 = 10'))  # Should print: 5.0
    print(tentacle('3*x - 2 = 1'))  # Should print: 1.0
    print(tentacle('2*x = 6'))  # Should print: 3.0
    print(tentacle('x = 5'))  # Should print: 5.0
    print(tentacle('2*x + 3 = 3*x'))  # Should print: -3.0
    print(tentacle('2*x + y = 7'))  # Should print: Error: Equation does not contain x
    print(tentacle('2*x + 3 ='))  # Should print: Error: Invalid equation format
    print(tentacle('0*x + 3 = 7'))  # Should print: Error: Coefficient of x is zero
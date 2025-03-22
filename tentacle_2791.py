# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.
    
    Args:
    equation (str): A string containing a linear equation in the form 'ax + b = c'.
    
    Returns:
    str: The solution for x as a string, or an error message if the equation cannot be solved.
    
    Example:
    >>> tentacle('2*x + 3 = 7')
    '2.0'
    """
    try:
        # Split the equation into left and right sides
        left, right = equation.split('=')
        
        # Remove whitespace
        left = left.strip()
        right = right.strip()
        
        # Parse the left side to extract coefficients
        if '+' in left:
            terms = left.split('+')
            if len(terms) == 2:
                if 'x' in terms[0]:
                    a = float(terms[0].replace('x', '').strip())
                    b = float(terms[1].strip())
                elif 'x' in terms[1]:
                    a = float(terms[1].replace('x', '').strip())
                    b = float(terms[0].strip())
                else:
                    return "Error: Invalid equation format"
            else:
                return "Error: Invalid equation format"
        elif '-' in left:
            terms = left.split('-')
            if len(terms) == 2:
                if 'x' in terms[0]:
                    a = float(terms[0].replace('x', '').strip())
                    b = -float(terms[1].strip())
                elif 'x' in terms[1]:
                    a = -float(terms[1].replace('x', '').strip())
                    b = float(terms[0].strip())
                else:
                    return "Error: Invalid equation format"
            else:
                return "Error: Invalid equation format"
        elif 'x' in left:
            a = float(left.replace('x', '').strip())
            b = 0
        else:
            return "Error: Invalid equation format"
        
        # Solve for x
        c = float(right)
        x = (c - b) / a
        
        return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('5*x - 4 = 6'))  # Should print: 2.0
    print(tentacle('x + 2 = 5'))    # Should print: 3.0
    print(tentacle('3*x = 9'))      # Should print: 3.0
    print(tentacle('2*x + 3 = 3'))  # Should print: 0.0
    print(tentacle('invalid'))      # Should print an error message
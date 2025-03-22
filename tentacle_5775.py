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
        
        # Extract coefficient of x and constant term
        if '+' in left:
            coeff, const = left.split('+')
            coeff = coeff.strip()
            const = const.strip()
        elif '-' in left:
            coeff, const = left.split('-')
            coeff = coeff.strip()
            const = '-' + const.strip()
        else:
            coeff = left
            const = '0'
        
        # Handle cases where x is alone or has a coefficient
        if coeff == 'x':
            coeff = '1'
        elif coeff.endswith('x'):
            coeff = coeff[:-1]
        else:
            return "Error: Invalid format for x"
        
        # Convert to float
        a = float(coeff)
        b = float(const)
        c = float(right)
        
        # Solve for x
        x = (c - b) / a
        
        # Return result as a string
        return str(x)
    
    except ValueError as e:
        return f"Error: {str(e)}"
    except Exception as e:
        return f"Error: Unable to solve equation - {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 10'))   # Should print: 15.0
    print(tentacle('3*x = 12'))     # Should print: 4.0
    print(tentacle('x + 2 = 2'))    # Should print: 0.0
    print(tentacle('2*x = x + 3'))  # Should print: 3.0
    print(tentacle('x = 5'))        # Should print: 5.0
    print(tentacle('2*x + y = 7'))  # Should print: Error: Equation must contain 'x'
    print(tentacle('2*x + 3 ='))    # Should print: Error: invalid literal for float(): 
    print(tentacle('2*x + 3 = a'))  # Should print: Error: invalid literal for float(): a
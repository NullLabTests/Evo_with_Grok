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
        # Split the equation into left and right sides
        left, right = equation.split('=')
        
        # Remove whitespace
        left = left.strip()
        right = right.strip()
        
        # Parse the left side to separate the coefficient and constant
        if '+' in left:
            left_parts = left.split('+')
            if len(left_parts) != 2:
                raise ValueError("Invalid equation format")
            coeff_part, const_part = left_parts
        elif '-' in left:
            left_parts = left.split('-')
            if len(left_parts) != 2:
                raise ValueError("Invalid equation format")
            coeff_part, const_part = left_parts
            const_part = '-' + const_part
        else:
            coeff_part = left
            const_part = '0'
        
        # Extract the coefficient of x
        if coeff_part.strip() == 'x':
            coeff = 1
        elif coeff_part.strip() == '-x':
            coeff = -1
        elif coeff_part.strip().endswith('x'):
            coeff = float(coeff_part.strip()[:-1])
        else:
            raise ValueError("Invalid equation format")
        
        # Convert constants to floats
        const = float(const_part)
        right_val = float(right)
        
        # Solve for x
        x = (right_val - const) / coeff
        
        # Return the result as a string
        return str(x)
    
    except Exception as e:
        # Return an error message if solving fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('5x - 2 = 8'))   # Should print: 2.0
    print(tentacle('-x + 4 = 1'))   # Should print: 3.0
    print(tentacle('x = 5'))        # Should print: 5.0
    print(tentacle('2x = 6'))       # Should print: 3.0
    print(tentacle('invalid'))      # Should print an error message
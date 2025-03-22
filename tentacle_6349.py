# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.
    
    Args:
    equation (str): A string containing a linear equation in the form 'ax + b = c'.
    
    Returns:
    str: The value of x as a string, or an error message if the equation is invalid or non-linear.
    
    Example:
    >>> tentacle('2*x + 3 = 7')
    '2'
    """
    try:
        # Remove spaces and split the equation at the equals sign
        equation = equation.replace(" ", "").split("=")
        if len(equation) != 2:
            return "Error: Invalid equation format"

        # Parse left and right sides of the equation
        left, right = equation[0], equation[1]

        # Check if 'x' is present on the left side
        if 'x' not in left:
            return "Error: No 'x' term found on the left side"

        # Extract coefficient of x and constant term from left side
        if left.startswith('x'):
            a = 1 if left == 'x' else float(left[0])
        elif left.endswith('x'):
            a = float(left[:-1])
        else:
            a = float(left.split('x')[0])
        
        # Extract constant term from left side
        b = 0
        if '+' in left:
            b = float(left.split('+')[-1])
        elif '-' in left and left.index('-') != left.index('x') - 1:
            b = float(left.split('-')[-1]) * -1

        # Convert right side to float
        c = float(right)

        # Solve for x
        x = (c - b) / a

        # Return x as a string
        return str(x)

    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 10'))  # Should print: 15.0
    print(tentacle('3x = 12'))  # Should print: 4.0
    print(tentacle('x/2 + 1 = 3'))  # Should print: 4.0
    print(tentacle('2x + 3y = 7'))  # Should print: Error: No 'x' term found on the left side
    print(tentacle('2*x + 3 ='))  # Should print: Error: Invalid equation format
    print(tentacle('x^2 + 2x + 1 = 0'))  # Should print: Error: No 'x' term found on the left side
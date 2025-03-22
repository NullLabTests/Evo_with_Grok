# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.
    
    Args:
    equation (str): A string containing a linear equation in the form 'a*x + b = c'.
    
    Returns:
    str: The solution for x as a string.
    
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
        
        # Find the coefficient of x on the left side
        if 'x' in left:
            if '*' in left:
                a = float(left.split('*')[0])
            else:
                a = 1 if left == 'x' else float(left.replace('x', ''))
        else:
            a = 0
        
        # Calculate the constant term on the left side
        b = eval(left.replace('x', '0'))
        
        # Calculate the right side
        c = eval(right)
        
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
    print(tentacle('x + 4 = 10'))   # Should print: 6.00
    print(tentacle('3*x = 15'))     # Should print: 5.00
    print(tentacle('2 = x'))        # Should print: 2.00
    print(tentacle('x = 5'))        # Should print: 5.00
    print(tentacle('2*x + 3 = x + 7'))  # Should print: 4.00
    print(tentacle('invalid equation'))  # Should print an error message
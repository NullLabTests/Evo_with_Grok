# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.
    
    Args:
    equation (str): A string containing a linear equation in the format 'ax + b = c'.
    
    Returns:
    str: The solution for x as a string, or an error message if the equation is invalid.
    
    Example:
    >>> tentacle('2*x + 3 = 7')
    '2'
    """
    try:
        # Split the equation into left and right sides
        left, right = equation.split('=')
        
        # Remove whitespace and simplify the equation
        left = left.strip().replace(' ', '')
        right = right.strip().replace(' ', '')
        
        # Extract coefficients and constants
        if 'x' in left:
            a, b = left.split('x') if '+' in left or '-' in left else [left.replace('x', ''), '0']
            a = float(a) if a and a != '-' else -1 if a == '-' else 1
            b = float(b) if b else 0
        else:
            return "Error: No 'x' term in the equation"
        
        c = float(right)
        
        # Solve for x
        x = (c - b) / a
        
        # Return the result rounded to 2 decimal places
        return f"{x:.2f}"
    
    except ValueError:
        return "Error: Invalid equation format"
    except ZeroDivisionError:
        return "Error: Division by zero"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.00
    print(tentacle('3*x - 5 = 10'))  # Should print: 5.00
    print(tentacle('x + 2 = 8'))  # Should print: 6.00
    print(tentacle('-x + 3 = 1'))  # Should print: 2.00
    print(tentacle('2*x = 6'))  # Should print: 3.00
    print(tentacle('x = 5'))  # Should print: 5.00
    print(tentacle('2*x + 3 = 3'))  # Should print: 0.00
    print(tentacle('2*x + 3 = 2*x + 3'))  # Should print: 0.00
    print(tentacle('2*x + 3 = 2*x + 4'))  # Should print: Error: Division by zero
    print(tentacle('invalid equation'))  # Should print: Error: Invalid equation format
    print(tentacle('2 + 3 = 5'))  # Should print: Error: No 'x' term in the equation
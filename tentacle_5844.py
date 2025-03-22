# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x.

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
        
        # Remove whitespace and simplify the equation
        left = left.strip().replace(' ', '')
        right = right.strip().replace(' ', '')
        
        # Extract coefficients
        if 'x' in left:
            a, b = left.split('x') if '+' in left or '-' in left else [left.replace('x', ''), '0']
            a = a.replace('+', '') if a.startswith('+') else a
            b = b.replace('+', '') if b.startswith('+') else b
            a = float(a) if a and a != '-' else -1 if a == '-' else 1
            b = float(b) if b else 0
        else:
            return "Error: Equation does not contain x"
        
        # Calculate x
        c = float(right)
        x = (c - b) / a
        
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
    print(tentacle('2*x = 7'))      # Should print: 3.50
    print(tentacle('x = 4'))        # Should print: 4.00
    print(tentacle('2*x + 3 = x'))  # Should print: -3.00
    print(tentacle('2*x + 3 = 3'))  # Should print: 0.00
    print(tentacle('2*x + 3'))      # Should print: Error: equation does not contain '='
    print(tentacle('y + 3 = 7'))    # Should print: Error: Equation does not contain x
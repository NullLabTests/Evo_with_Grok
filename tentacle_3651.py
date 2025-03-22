# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x.

    Args:
    equation (str): A string containing a linear equation in the format 'ax + b = c'.

    Returns:
    str: The solution for x as a string.

    Example:
    >>> tentacle('2*x + 3 = 7')
    '2'
    """
    try:
        # Split the equation into left and right sides
        left, right = equation.split('=')
        
        # Remove spaces and evaluate both sides
        left = left.replace(' ', '').replace('x', '*x')
        right = right.replace(' ', '')
        
        # Parse the left side to extract coefficients
        import re
        left_parts = re.split(r'([+\-])', left)
        left_parts = [part for part in left_parts if part]
        
        a = 0
        b = 0
        for i in range(0, len(left_parts), 2):
            term = left_parts[i]
            if 'x' in term:
                coef = term.replace('x', '').replace('*', '')
                a += float(coef) if coef else 1
                if i > 0 and left_parts[i-1] == '-':
                    a *= -1
            else:
                const = float(term)
                b += const if i == 0 or left_parts[i-1] == '+' else -const
        
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
    print(tentacle('5*x - 10 = 0'))  # Should print: 2.00
    print(tentacle('-3*x + 4 = 1'))  # Should print: 1.00
    print(tentacle('x/2 + 3 = 5'))  # Should print: 4.00
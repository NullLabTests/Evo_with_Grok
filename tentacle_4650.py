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
        
        # Remove whitespace and simplify the equation
        left = left.strip().replace(' ', '')
        right = right.strip().replace(' ', '')
        
        # Find the coefficient of x (a) and the constant term (b) on the left side
        if 'x' in left:
            if left == 'x':
                a = 1
                b = 0
            elif left.startswith('-x'):
                a = -1
                b = 0
            elif left.startswith('x'):
                a = 1
                b = 0
            else:
                if '+' in left:
                    a_part, b_part = left.split('+')
                elif '-' in left and left.index('-') != 0:
                    a_part, b_part = left.split('-')
                    b_part = '-' + b_part
                else:
                    a_part = left
                    b_part = '0'
                
                if a_part.endswith('x'):
                    a = float(a_part[:-1])
                elif a_part.startswith('-') and a_part[1:].endswith('x'):
                    a = float(a_part[:-1])
                else:
                    raise ValueError("Invalid equation format")
                
                b = float(b_part)
        else:
            a = 0
            b = float(left)
        
        # Calculate c from the right side
        c = float(right)
        
        # Solve for x
        if a == 0 and b == c:
            return 'Infinite solutions'
        elif a == 0 and b != c:
            return 'No solution'
        else:
            x = (c - b) / a
            return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 10'))   # Should print: 15.0
    print(tentacle('-3*x = 9'))     # Should print: -3.0
    print(tentacle('2 = 2'))        # Should print: Infinite solutions
    print(tentacle('2 = 3'))        # Should print: No solution
    print(tentacle('x + x = 2'))    # Should print: 1.0
    print(tentacle('2*x + 3 = x'))  # Should print: -3.0
    print(tentacle('invalid'))      # Should print: Error: ...
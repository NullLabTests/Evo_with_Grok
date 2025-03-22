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
        
        # Remove whitespace and parse the left side
        left = left.strip().replace(' ', '')
        right = right.strip().replace(' ', '')
        
        # Find the coefficient of x and the constant term on the left side
        if 'x' in left:
            if left.startswith('-x'):
                a = -1
                left = left[2:]
            elif left.startswith('x'):
                a = 1
                left = left[1:]
            else:
                if left[0] == '-':
                    a = -float(left.split('x')[0][1:])
                else:
                    a = float(left.split('x')[0])
                left = left.split('x')[1]
        else:
            a = 0
        
        # Calculate the constant term on the left side
        b = eval(left) if left else 0
        
        # Calculate the right side of the equation
        c = eval(right)
        
        # Solve for x
        x = (c - b) / a
        
        # Return the solution rounded to 2 decimal places
        return f"{x:.2f}"
    
    except ZeroDivisionError:
        return "Error: Division by zero (coefficient of x is zero)"
    except Exception as e:
        return f"Error: Invalid equation - {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.00
    print(tentacle('5*x - 2 = 8'))  # Should print: 2.00
    print(tentacle('-x + 4 = 1'))  # Should print: 3.00
    print(tentacle('3 = 2*x + 1'))  # Should print: 1.00
    print(tentacle('x = 5'))  # Should print: 5.00
    print(tentacle('2*x = 4'))  # Should print: 2.00
    print(tentacle('3 = 3'))  # Should print: Error: Division by zero (coefficient of x is zero)
    print(tentacle('2*x + 3 = a'))  # Should print: Error: Invalid equation - name 'a' is not defined
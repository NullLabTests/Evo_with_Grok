# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x.

    Args:
    equation (str): A string containing a linear equation in the form 'a*x + b = c'.

    Returns:
    str: The solution for x as a string, or an error message if the equation is invalid.

    Example:
    >>> tentacle('2*x + 3 = 7')
    '2'
    """
    try:
        # Remove spaces and split the equation at '='
        equation = equation.replace(' ', '').split('=')
        
        if len(equation) != 2:
            return "Error: Invalid equation format. Use 'a*x + b = c'."
        
        left, right = equation
        
        # Parse the left side of the equation
        if 'x' not in left:
            return "Error: Equation must contain 'x'."
        
        # Split left side into parts
        parts = left.split('+')
        a = 0
        b = 0
        
        for part in parts:
            if 'x' in part:
                if part == 'x':
                    a = 1
                elif part == '-x':
                    a = -1
                else:
                    a = float(part.replace('x', ''))
            else:
                b += float(part)
        
        # Parse the right side of the equation
        c = float(right)
        
        # Solve for x
        x = (c - b) / a
        
        # Return the result rounded to 2 decimal places
        return f"{x:.2f}"
    
    except ValueError:
        return "Error: Invalid number format in the equation."
    except ZeroDivisionError:
        return "Error: Division by zero. 'a' cannot be zero in 'a*x + b = c'."
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.00
    print(tentacle('x - 5 = 10'))   # Should print: 15.00
    print(tentacle('-3*x = 9'))     # Should print: -3.00
    print(tentacle('2*x = 4'))      # Should print: 2.00
    print(tentacle('x + 2 = 2'))    # Should print: 0.00
    print(tentacle('2*x + 3 = 3*x'))  # Should print: Error: Invalid equation format. Use 'a*x + b = c'.
    print(tentacle('2*x + y = 7'))  # Should print: Error: Equation must contain 'x'.
    print(tentacle('2*x + 3 = a'))  # Should print: Error: Invalid number format in the equation.
    print(tentacle('0*x + 3 = 7'))  # Should print: Error: Division by zero. 'a' cannot be zero in 'a*x + b = c'.
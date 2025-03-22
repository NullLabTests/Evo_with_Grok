# Domains: text processing, mathematics
def tentacle(equation):
    """
    Solve a linear equation for x given as a string.
    
    Args:
    equation (str): A string containing a linear equation in the form 'a*x + b = c'.
    
    Returns:
    str: The solution for x as a string, or an error message if the equation is invalid.
    
    Example:
    >>> tentacle('2*x + 3 = 7')
    '2'
    """
    try:
        # Remove spaces and split the equation into left and right sides
        equation = equation.replace(" ", "")
        left, right = equation.split("=")
        
        # Parse the left side of the equation
        if '+' in left:
            a_part, b_part = left.split("+")
        elif '-' in left:
            a_part, b_part = left.split("-")
            b_part = "-" + b_part
        else:
            a_part = left
            b_part = "0"
        
        # Extract coefficient 'a' of x
        if a_part.endswith("x"):
            a = a_part[:-1] if a_part != "x" else "1"
        elif a_part.startswith("x"):
            a = a_part[1:] if a_part != "x" else "1"
        else:
            raise ValueError("Invalid equation format")
        
        # Convert a and b to floats
        a = float(eval(a))
        b = float(eval(b_part))
        c = float(eval(right))
        
        # Solve for x
        x = (c - b) / a
        
        # Return the solution as a string
        return str(x)
    
    except Exception as e:
        # Return an error message if solving fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 10'))   # Should print: 15.0
    print(tentacle('-3*x = 9'))     # Should print: -3.0
    print(tentacle('2*x = 4'))      # Should print: 2.0
    print(tentacle('x + 2 = 3'))    # Should print: 1.0
    print(tentacle('2*x + 3 = x'))  # Should print: -3.0
    print(tentacle('invalid'))      # Should print an error message
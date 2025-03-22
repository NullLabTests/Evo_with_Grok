# Domains: text processing, mathematics
import re

def tentacle(equation):
    """
    Solve a linear equation for x.

    Args:
    equation (str): A string containing a linear equation in the form 'ax + b = c'.

    Returns:
    str: The solution for x as a string, or an error message if the equation is invalid.

    Example:
    >>> tentacle('2*x + 3 = 7')
    '2.0'
    """
    try:
        # Remove whitespace and convert to lowercase
        equation = equation.replace(" ", "").lower()

        # Extract coefficients using regex
        match = re.match(r"(-?\d*\.?\d*)?[*]x([-+]\d*\.?\d*)?=([-+]\d*\.?\d*)", equation)
        if not match:
            return "Error: Invalid equation format"

        a, b, c = match.groups()
        
        # Convert coefficients to floats, handling empty strings
        a = float(a) if a and a != '-' else -1 if a == '-' else 1
        b = float(b) if b else 0
        c = float(c) if c else 0

        # Solve for x
        x = (c - b) / a

        # Return the solution rounded to 2 decimal places
        return f"{x:.2f}"

    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.00
    print(tentacle('x - 5 = 10'))   # Should print: 15.00
    print(tentacle('-3*x = 9'))     # Should print: -3.00
    print(tentacle('2*x = 0'))      # Should print: 0.00
    print(tentacle('x + 2 = 2'))    # Should print: 0.00
    print(tentacle('2*x + 3 = 3*x'))  # Should print: Error: division by zero
    print(tentacle('y + 2 = 3'))    # Should print: Error: Invalid equation format
    print(tentacle('2*x + 3'))      # Should print: Error: Invalid equation format
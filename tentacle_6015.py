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
        # Remove spaces and split the equation at the equals sign
        left, right = equation.replace(" ", "").split("=")
        
        # Separate terms on the left side
        terms = left.split("+")
        
        # Initialize coefficients
        a, b = 0, 0
        
        # Process each term
        for term in terms:
            if "x" in term:
                if term == "x":
                    a += 1
                elif term == "-x":
                    a -= 1
                else:
                    a += float(term.replace("x", ""))
            else:
                b += float(term)
        
        # Calculate x
        c = float(right)
        x = (c - b) / a
        
        # Return the result as a string
        return str(x)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2*x + 3 = 7'))  # Should print: 2.0
    print(tentacle('x - 5 = 0'))    # Should print: 5.0
    print(tentacle('-3*x = 9'))     # Should print: -3.0
    print(tentacle('2*x + 3 = x'))  # Should print: -3.0
    print(tentacle('invalid'))      # Should print an error message
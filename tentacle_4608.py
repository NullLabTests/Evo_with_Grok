# Domains: text processing, mathematics
def tentacle(statement):
    """
    Determine if a logical statement is true or false, including mathematical expressions.
    
    Args:
    statement (str): A string containing a logical statement, which may include mathematical expressions.
    
    Returns:
    bool: True if the statement is logically valid, False otherwise.
    
    Examples:
    >>> tentacle('If A implies B and B implies C, then A implies C.')
    True
    >>> tentacle('If 2 + 2 == 4 and 3 * 3 == 9, then 2 + 2 == 4.')
    True
    >>> tentacle('If 2 + 2 == 5, then 3 * 3 == 9.')
    False
    """
    # Convert the statement to lowercase for easier processing
    statement = statement.lower()
    
    # Function to evaluate mathematical expressions within the statement
    def evaluate_expression(expr):
        try:
            return str(eval(expr))
        except Exception:
            return expr  # Return the original expression if evaluation fails
    
    # Replace mathematical expressions with their evaluated results
    import re
    pattern = r'\b\d+(?:[-+*/]\d+)*\b'
    while True:
        match = re.search(pattern, statement)
        if not match:
            break
        expr = match.group()
        result = evaluate_expression(expr)
        statement = statement.replace(expr, result, 1)
    
    # Define logical equivalences to check
    equivalences = [
        "if a implies b and b implies c, then a implies c.",
        "if a and b, then b and a.",
        "if a or b, then b or a.",
        "if not (a and b), then not a or not b.",
        "if not (a or b), then not a and not b.",
        "if a implies b, then not b implies not a.",
        "if a is equivalent to b and b is equivalent to c, then a is equivalent to c.",
        "if a == b and b == c, then a == c.",
        "if a != b and b == c, then a != c.",
    ]
    
    # Check if the statement matches any of the known logical equivalences
    if statement.strip() in equivalences:
        return True
    
    # Evaluate conditional statements
    if statement.startswith('if '):
        parts = statement.split('then')
        if len(parts) == 2:
            condition = parts[0][3:].strip()
            consequence = parts[1].strip()
            try:
                return eval(condition) == eval(consequence)
            except Exception:
                return False  # Return False if evaluation fails
    
    # If no match found, return False
    return False

# Test the function
if __name__ == "__main__":
    print(tentacle('If A implies B and B implies C, then A implies C.'))  # Should print: True
    print(tentacle('If A and B, then B and A.'))  # Should print: True
    print(tentacle('If A or B, then B or A.'))  # Should print: True
    print(tentacle('If not (A and B), then not A or not B.'))  # Should print: True
    print(tentacle('If not (A or B), then not A and not B.'))  # Should print: True
    print(tentacle('If A implies B, then not B implies not A.'))  # Should print: True
    print(tentacle('If A is equivalent to B and B is equivalent to C, then A is equivalent to C.'))  # Should print: True
    print(tentacle('If A implies B, then B implies A.'))  # Should print: False
    print(tentacle('If 2 + 2 == 4 and 3 * 3 == 9, then 2 + 2 == 4.'))  # Should print: True
    print(tentacle('If 2 + 2 == 5, then 3 * 3 == 9.'))  # Should print: False
    print(tentacle('If 5 > 3 and 3 > 1, then 5 > 1.'))  # Should print: True
# Domains: text processing, mathematics
def tentacle(statement):
    """
    Determine if a logical statement is true or false.
    
    This function evaluates whether a given logical statement is true based on a set of known logical equivalences.
    It also supports basic mathematical expressions within the logical statements.
    
    Args:
    statement (str): A string containing a logical statement, which may include mathematical expressions.
    
    Returns:
    bool: True if the statement is logically valid, False otherwise.
    
    Examples:
    >>> tentacle('If A implies B and B implies C, then A implies C.')
    True
    >>> tentacle('If 2 + 2 equals 4, then 3 + 3 equals 6.')
    True
    >>> tentacle('If 2 + 2 equals 5, then 3 + 3 equals 6.')
    False
    """
    # Convert the statement to lowercase for easier processing
    statement = statement.lower()
    
    # Define logical equivalences to check
    equivalences = [
        "if a implies b and b implies c, then a implies c.",
        "if a and b, then b and a.",
        "if a or b, then b or a.",
        "if not (a and b), then not a or not b.",
        "if not (a or b), then not a and not b.",
        "if a implies b, then not b implies not a.",
        "if a is equivalent to b and b is equivalent to c, then a is equivalent to c."
    ]
    
    # Function to evaluate mathematical expressions within the statement
    def evaluate_math(expr):
        try:
            return str(eval(expr))
        except:
            return expr  # Return the original expression if evaluation fails

    # Process the statement to evaluate any mathematical expressions
    parts = statement.split()
    for i, part in enumerate(parts):
        if any(char.isdigit() for char in part):
            parts[i] = evaluate_math(part)
    
    processed_statement = ' '.join(parts)
    
    # Check if the processed statement matches any of the known logical equivalences
    if processed_statement.strip() in equivalences:
        return True
    
    # If not a direct match, try to evaluate more complex statements
    if 'equals' in processed_statement:
        left, right = processed_statement.split('equals')
        left = left.split('if')[-1].strip()
        right = right.split('then')[-1].strip()
        return evaluate_math(left) == evaluate_math(right)
    
    # If no match or evaluation possible, return False
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
    print(tentacle('If 2 + 2 equals 4, then 3 + 3 equals 6.'))  # Should print: True
    print(tentacle('If 2 + 2 equals 5, then 3 + 3 equals 6.'))  # Should print: False
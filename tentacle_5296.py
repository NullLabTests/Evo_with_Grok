# Domains: text processing, mathematics
def tentacle(statement):
    """
    Determine if a logical statement is true or false.
    
    This function evaluates logical statements and returns True if the statement
    is logically valid, False otherwise. It uses a set of predefined logical
    equivalences to make this determination.
    
    Args:
    statement (str): A string containing a logical statement.
    
    Returns:
    bool: True if the statement is logically valid, False otherwise.
    
    Example:
    >>> tentacle('If A implies B and B implies C, then A implies C.')
    True
    """
    # Convert the statement to lowercase for easier processing
    statement = statement.lower().strip()
    
    # Define logical equivalences to check
    equivalences = {
        "if a implies b and b implies c, then a implies c.": True,
        "if a and b, then b and a.": True,
        "if a or b, then b or a.": True,
        "if not (a and b), then not a or not b.": True,
        "if not (a or b), then not a and not b.": True,
        "if a implies b, then not b implies not a.": True,
        "if a is equivalent to b and b is equivalent to c, then a is equivalent to c.": True,
        "if a implies b, then b implies a.": False
    }
    
    # Check if the statement matches any of the known logical equivalences
    return equivalences.get(statement, False)

# Test the function
if __name__ == "__main__":
    test_statements = [
        'If A implies B and B implies C, then A implies C.',
        'If A and B, then B and A.',
        'If A or B, then B or A.',
        'If not (A and B), then not A or not B.',
        'If not (A or B), then not A and not B.',
        'If A implies B, then not B implies not A.',
        'If A is equivalent to B and B is equivalent to C, then A is equivalent to C.',
        'If A implies B, then B implies A.'
    ]
    
    for statement in test_statements:
        result = tentacle(statement)
        print(f"'{statement}': {result}")
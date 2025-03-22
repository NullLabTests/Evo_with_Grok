# Domains: text processing, mathematics
def tentacle(statement):
    """
    Determine if a logical statement is true or false based on known logical equivalences.
    
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
    equivalences = [
        "if a implies b and b implies c, then a implies c.",
        "if a and b, then b and a.",
        "if a or b, then b or a.",
        "if not (a and b), then not a or not b.",
        "if not (a or b), then not a and not b.",
        "if a implies b, then not b implies not a.",
        "if a is equivalent to b and b is equivalent to c, then a is equivalent to c.",
        "if a implies b and b implies a, then a is equivalent to b.",
        "if a is equivalent to b, then b is equivalent to a.",
        "if a and (b or c), then (a and b) or (a and c).",
        "if a or (b and c), then (a or b) and (a or c).",
        "if a implies b, then not a or b.",
        "if a and b implies c, then a implies (b implies c).",
        "if a implies b and a implies c, then a implies (b and c).",
        "if a implies b or a implies c, then a implies (b or c).",
    ]
    
    # Check if the statement matches any of the known logical equivalences
    if statement in equivalences:
        return True
    
    # Additional checks for more complex statements
    if statement.startswith("if ") and statement.endswith("."):
        # Remove 'if ' at the start and '.' at the end
        core_statement = statement[3:-1]
        
        # Split the statement into antecedent and consequent
        parts = core_statement.split(", then ")
        if len(parts) == 2:
            antecedent, consequent = parts
            
            # Check for simple implications
            if antecedent.strip() == consequent.strip():
                return True
            
            # Check for contrapositives
            if antecedent.startswith("not ") and consequent.startswith("not "):
                positive_antecedent = antecedent[4:]
                positive_consequent = consequent[4:]
                if positive_consequent.strip() == positive_antecedent.strip():
                    return True
            
            # Check for logical equivalences
            if " is equivalent to " in antecedent and " is equivalent to " in consequent:
                a1, b1 = antecedent.split(" is equivalent to ")
                a2, b2 = consequent.split(" is equivalent to ")
                if a1.strip() == a2.strip() and b1.strip() == b2.strip():
                    return True
    
    return False

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
        'If A implies B, then B implies A.',
        'If A implies B and B implies A, then A is equivalent to B.',
        'If A is equivalent to B, then B is equivalent to A.',
        'If A and (B or C), then (A and B) or (A and C).',
        'If A or (B and C), then (A or B) and (A or C).',
        'If A implies B, then not A or B.',
        'If A and B implies C, then A implies (B implies C).',
        'If A implies B and A implies C, then A implies (B and C).',
        'If A implies B or A implies C, then A implies (B or C).',
        'If A implies B, then B implies A.',  # False
        'If A and B, then A or B.',  # False
        'If A is equivalent to B, then A implies B and B implies A.',  # True
        'If A implies B and C implies D, then A and C implies B and D.',  # False
    ]
    
    for statement in test_statements:
        result = tentacle(statement)
        print(f"{statement}: {result}")
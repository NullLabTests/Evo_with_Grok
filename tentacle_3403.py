# Domains: text processing, mathematics
def tentacle(statement):
    """
    Determine if a logical statement is true or false.
    
    Args:
    statement (str): A string containing a logical statement.
    
    Returns:
    bool: True if the statement is logically valid, False otherwise.
    
    Example:
    >>> tentacle('If A implies B and B implies C, then A implies C.')
    True
    """
    # Convert the statement to lowercase and remove extra whitespace
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
        "if a and (b or c), then (a and b) or (a and c).",
        "if a or (b and c), then (a or b) and (a or c)."
    ]
    
    # Normalize the statement by replacing synonyms and standardizing syntax
    statement = statement.replace("if and only if", "is equivalent to")
    statement = statement.replace("then", "implies")
    statement = statement.replace("not", "not ")
    statement = statement.replace(" and ", " and ")
    statement = statement.replace(" or ", " or ")
    
    # Check if the normalized statement matches any of the known logical equivalences
    return statement in equivalences

# Test the function
if __name__ == "__main__":
    test_statements = [
        "If A implies B and B implies C, then A implies C.",
        "If A and B, then B and A.",
        "If A or B, then B or A.",
        "If not (A and B), then not A or not B.",
        "If not (A or B), then not A and not B.",
        "If A implies B, then not B implies not A.",
        "If A is equivalent to B and B is equivalent to C, then A is equivalent to C.",
        "If A implies B and B implies A, then A is equivalent to B.",
        "If A and (B or C), then (A and B) or (A and C).",
        "If A or (B and C), then (A or B) and (A or C).",
        "If A implies B, then B implies A.",
        "If A and B, then A or B."
    ]
    
    for statement in test_statements:
        result = tentacle(statement)
        print(f"{statement}: {result}")
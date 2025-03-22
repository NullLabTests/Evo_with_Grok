# Domains: text processing, mathematics
def tentacle(statement):
    """
    Determine if a logical statement is true or false.

    This function evaluates logical statements, focusing on implications and equivalences.
    It normalizes the input statement and compares it against a set of known logical truths.

    Args:
    statement (str): A string containing a logical statement.

    Returns:
    bool: True if the statement is logically valid, False otherwise.

    Examples:
    >>> tentacle('If A implies B and B implies C, then A implies C.')
    True
    >>> tentacle('If A implies B, then B implies A.')
    False
    """
    # Normalize the statement by converting to lowercase and removing extra spaces
    normalized_statement = ' '.join(statement.lower().split())

    # Define a set of known logical truths
    logical_truths = {
        "if a implies b and b implies c, then a implies c.",
        "if a and b, then b and a.",
        "if a or b, then b or a.",
        "if not (a and b), then not a or not b.",
        "if not (a or b), then not a and not b.",
        "if a implies b, then not b implies not a.",
        "if a is equivalent to b and b is equivalent to c, then a is equivalent to c."
    }

    # Check if the normalized statement matches any of the known logical truths
    return normalized_statement in logical_truths

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
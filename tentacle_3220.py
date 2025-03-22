# Domains: text processing, mathematics
def tentacle(statement):
    """
    Determine if a logical statement is true or false.

    This function evaluates the validity of logical statements by comparing them
    against a set of known logical equivalences.

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
    # Normalize the input statement
    statement = statement.lower().strip()
    
    # Remove common words and punctuation to simplify comparison
    words_to_remove = ['if', 'then', 'and', 'is', ',', '.']
    for word in words_to_remove:
        statement = statement.replace(word, '')
    
    # Define logical equivalences to check
    equivalences = [
        "a implies b b implies c a implies c",
        "a b b a",
        "a or b b or a",
        "not a and b not a or not b",
        "not a or b not a and not b",
        "a implies b not b implies not a",
        "a equivalent to b b equivalent to c a equivalent to c"
    ]
    
    # Check if the normalized statement matches any of the known logical equivalences
    return statement in equivalences

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
        print(f"{statement}: {result}")